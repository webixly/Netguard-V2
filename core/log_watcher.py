import os
import re
import time
import requests

THREAT_MATRIX = {
    "Brute Force": {
        "pattern": re.compile(r"failed|unauthorized|invalid user|access denied|bad password", re.IGNORECASE),
        "severity": "🔴 HIGH"
    },
    "Port Scan & Recon": {
        "pattern": re.compile(r"scan|nmap|probe|connection refused|port\s?\d+\s?closed", re.IGNORECASE),
        "severity": "🟡 MEDIUM"
    },
    "SQL Injection (SQLi)": {
        "pattern": re.compile(r"union\s+select|select\s+.*\s+from|insert\s+into|drop\s+table|'--", re.IGNORECASE),
        "severity": "⚫ CRITICAL"
    },
    "Cross-Site Scripting (XSS)": {
        "pattern": re.compile(r"<script>|javascript:|alert\(|onerror=", re.IGNORECASE),
        "severity": "🔴 HIGH"
    },
    "Directory Traversal": {
        "pattern": re.compile(r"\.\./|\.\.\\|etc/passwd", re.IGNORECASE),
        "severity": "🔴 HIGH"
    },
    "Command Injection (RCE)": {
        "pattern": re.compile(r";\s*cat\s+/|\|\s*wget|&&\s*curl|;\s*id|;\s*whoami", re.IGNORECASE),
        "severity": "⚫ CRITICAL"
    },
    "Log4Shell Vulnerability": {
        "pattern": re.compile(r"\$\{\s*jndi\s*:\s*(rmi|ldap|ldaps|http|https|dns)\s*:", re.IGNORECASE),
        "severity": "⚫ CRITICAL"
    },
    "Cryptomining Activity": {
        "pattern": re.compile(r"stratum\+tcp|minerd|xmrig", re.IGNORECASE),
        "severity": "🟡 MEDIUM"
    },
    "DoS / Resource Stress": {
        "pattern": re.compile(r"out of memory|oom-killer|maximum connection limit reached", re.IGNORECASE),
        "severity": "🔴 HIGH"
    }
}

stats = {
    "threats_today": 0,
    "critical": 0,
    "high": 0,
    "medium": 0,
    "info": 0,
    "counters": {
        "Brute Force": 0,
        "SQLi": 0,
        "XSS": 0,
        "Recon": 0,
        "DoS": 0
    },
    "webhook_count": 0
}

DISCORD_WEBHOOK_URL = "" 

def send_discord_alert(attack_type: str, severity: str, log_line: str) -> bool:
    """ترسل تنبيهاً فورياً منسقاً إلى ديسكورد وترجع True في حال النجاح"""
    if not DISCORD_WEBHOOK_URL:
        return False

    payload = {
        "embeds": [
            {
                "title": f"🚨 NetGuard V2 Alert: {attack_type} ({severity})",
                "description": f"```text\n{log_line.strip()}\n```",
                "color": 15158332 if "HIGH" in severity or "CRITICAL" in severity else 15105570,
                "footer": {"text": "NetGuard SOC Engine"},
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
            }
        ]
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=2)
        return response.status_code == 204
    except Exception:
        return False

def colorize_log_elements(line: str) -> str:
    """تلوين الوقت والـ IP ونوع الخدمة داخل أسطر الـ Log لتسهيل القراءة"""
    
    line = re.sub(r"(\d{2}:\d{2}:\d{2})", r"[bold blue]\1[/bold blue]", line)
    line = re.sub(r"(\[[a-zA-Z0-9_-]+\])", r"[bold yellow]\1[/bold yellow]", line)
    line = re.sub(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", r"[bold cyan]\1[/bold cyan]", line)
    return line

def follow_log(file_path: str):
    """تراقب وتحلل السجلات حياً وتحدث العدادات والمستويات"""
    if not os.path.exists(file_path):
        yield f"[bold red]System Error:[/bold red] Log file '{file_path}' not found."
        return

    with open(file_path, "r") as f:
        while True:
            line = f.readline()
            if not line:
                yield None
                continue
            
            detected = False
            processed_line = colorize_log_elements(line.strip())
            
            for attack_name, data in THREAT_MATRIX.items():
                if data["pattern"].search(line):
                    severity = data["severity"]
                    
                    stats["threats_today"] += 1
                    if "⚫" in severity: stats["critical"] += 1
                    elif "🔴" in severity: stats["high"] += 1
                    elif "🟡" in severity: stats["medium"] += 1
                    
                    if attack_name == "Brute Force": stats["counters"]["Brute Force"] += 1
                    elif "SQL" in attack_name: stats["counters"]["SQLi"] += 1
                    elif "XSS" in attack_name: stats["counters"]["XSS"] += 1
                    elif "Recon" in attack_name: stats["counters"]["Recon"] += 1
                    elif "DoS" in attack_name: stats["counters"]["DoS"] += 1
                    
                    yield f"{severity} [bold red]ALERT[/bold red] | {processed_line}"
                    
                    if DISCORD_WEBHOOK_URL:
                        success = send_discord_alert(attack_name, severity, line)
                        if success:
                            stats["webhook_count"] += 1
                            yield f"[bold green]✔ Discord Notification Sent[/bold green] [gray](Alert #{stats['webhook_count']})[/gray]"
                    
                    detected = True
                    break
            
            if not detected:
                stats["info"] += 1
                yield f"🟢 LOW [gray]INFO[/gray]  | {processed_line}"
