import os
import re
import time
import requests


SUSPICIOUS_PATTERNS = {
    
    "Brute Force": re.compile(
        r"failed|unauthorized|invalid user|access denied|bad password|authentication failure|login_failed|permission denied", 
        re.IGNORECASE
    ),
    
    
    "Port Scan & Recon": re.compile(
        r"scan|nmap|probe|connection refused|port\s?\d+\s?closed|masscan|zgrab|syn flood|ping of death", 
        re.IGNORECASE
    ),
    
   
    "SQL Injection (SQLi)": re.compile(
        r"union\s+select|select\s+.*\s+from|insert\s+into|drop\s+table|'--|/\*|\bor\b\s+\d+=\d+|update\s+.*set|exec\s*\(", 
        re.IGNORECASE
    ),
    "Cross-Site Scripting (XSS)": re.compile(
        r"<script>|javascript:|alert\(|onerror=|onload=|document\.cookie|<img\s+src=.*onerror", 
        re.IGNORECASE
    ),
    "Directory Traversal": re.compile(
        r"\.\./|\.\.\\|etc/passwd|windows/system32|boot\.ini|win\.ini|proc/self/environ", 
        re.IGNORECASE
    ),
    
   
    "Sensitive File Access": re.compile(
        r"\.env|wp-config\.php|config\.json|config\.ini|credentials|id_rsa|master\.passwd|sam_file", 
        re.IGNORECASE
    ),
    
   
    "Web Shell & Backdoor": re.compile(
        r"shell\.php|cmd\.aspx|c99\.php|r57\.php|wsh\.php|eval\(base64_decode|system\(\$_GET|passthru\(", 
        re.IGNORECASE
    ),
    
    
    "Privilege Escalation": re.compile(
        r"sudo:\s+auth\s+failure|command\s+not\s+allowed|su:\s+auth\s+failed|privilege\s+escalation|rootkit|setuid\s+violation", 
        re.IGNORECASE
    ),
    
    
    "Command Injection (RCE)": re.compile(
        r";\s*cat\s+/|\|\s*wget|&&\s*curl|;\s*id|;\s*whoami|/bin/bash|/bin/sh|os\.system\(|popen\(", 
        re.IGNORECASE
    ),
    "Log4Shell Vulnerability": re.compile(
        r"\$\{\s*jndi\s*:\s*(rmi|ldap|ldaps|http|https|dns)\s*:", 
        re.IGNORECASE
    ),
    
   
    "Cryptomining Activity": re.compile(
        r"stratum\+tcp|minerd|xmrig|cryptonight|nicehash|pool\s+address", 
        re.IGNORECASE
    ),
    "DoS / Resource Exhaustion": re.compile(
        r"out of memory|oom-killer|too many open files|maximum connection limit reached|connection timed out", 
        re.IGNORECASE
    )
}


DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1528059030151364668/TErhfAZJ0EI1bkCiXukWYeW8ULAfHZMmiP8R_AEXXpJR2jTRsafcAgcsswLMZmmFaykS"

def send_discord_alert(attack_type: str, log_line: str) -> None:
    """ترسل تنبيهاً فورياً منسقاً إلى قناة ديسكورد عند اكتشاف هجوم"""
    if not DISCORD_WEBHOOK_URL:
        return  

    
    payload = {
        "embeds": [
            {
                "title": f"🚨 NetGuard Security Alert: {attack_type}",
                "description": f"```text\n{log_line.strip()}\n```",
                "color": 15158332, 
                "footer": {
                    "text": "NetGuard V2 Live Monitoring Engine"
                },
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
            }
        ]
    }

    try:
        
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=3)
    except Exception:
        pass  


def follow_log(file_path: str):
    """تراقب ملف اللوج حياً، وتحلله، وترسل تنبيهات خارجية عند الضرورة"""
    if not os.path.exists(file_path):
        yield f"[bold red]System Error:[/bold red] Log file '{file_path}' not found."
        return

    with open(file_path, "r") as f:
       
        # f.seek(0, 2) 
        
        while True:
            line = f.readline()
            if not line:
                yield None
                continue
            
            detected = False
            for attack_type, pattern in SUSPICIOUS_PATTERNS.items():
                if pattern.search(line):
                   
                    yield f"[bold red]🚨 ALERT [{attack_type}]:[/bold red] {line.strip()}"
                   
                    send_discord_alert(attack_type, line)
                    detected = True
                    break
            
            if not detected:
                yield f"[gray]INFO:[/gray] {line.strip()}"