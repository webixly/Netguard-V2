<div align="center">

# 🛡️ NetGuard V2

### Advanced Infrastructure Security Dashboard

Enterprise-grade Blue Team tool for monitoring Linux servers, detecting security threats, and visualizing system health in real-time.

<img src="images/Capture d'écran 2026-07-18 165947.png" width="900"/>

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Linux-Supported-black?style=for-the-badge&logo=linux)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

</div>

---

# 📖 Overview

NetGuard V2 is an advanced Blue Team monitoring dashboard that continuously analyzes Linux logs, monitors system resources, and instantly delivers security alerts to Discord whenever malicious activity is detected.
Unlike traditional log viewers, NetGuard V2 combines:

- 🔍 Threat Detection
- 📊 Live Infrastructure Monitoring
- 🚨 Instant Discord Alerts
- 🖥️ Rich Terminal Dashboard

into one lightweight terminal application.

---

# 🚨 Discord Alert System

NetGuard V2 supports **real-time Discord webhook notifications**, allowing security teams to receive instant alerts whenever suspicious activity is detected.

Instead of constantly monitoring terminal logs, administrators are notified immediately through a dedicated Discord channel.

### Alert Information

Each notification contains:

- 🚨 Threat Type
- 🌐 Source IP Address
- 📄 Log Entry
- ⏰ Detection Timestamp
- 🔥 Severity Level (Low / Medium / High)

### Example Notification

```text
🚨 SECURITY ALERT

Threat: SQL Injection
Severity: HIGH

Source IP:
192.168.1.55

Log:
GET /login.php?id=' OR 1=1--

Time:
2026-07-18 14:53 UTC
```

### Benefits

- Instant incident awareness
- Remote monitoring from any device
- Faster response time
- Team collaboration through Discord channels
- Works 24/7 without keeping the terminal open
# ✨ Features

## 🔐 Threat Detection

- SSH Brute Force Detection
- SQL Injection Detection
- XSS Detection
- Directory Traversal
- Web Shell Detection
- Remote Code Execution Patterns
- Log4Shell Detection
- Nmap Scan Detection
- Port Scan Detection
- DoS Indicators
- Crypto Miner Indicators

---

## 📊 Infrastructure Monitoring

- CPU Usage
- RAM Usage
- Disk Usage
- Color-coded Resource Status
- Live Updates

---

## 🚨 Alerting

- Discord Webhooks
- High Severity Alerts
- Threat Classification
- Real-time Notifications
- Discord Webhook Integration
- Instant Security Notifications
- Severity Classification
- Remote Monitoring
- Custom Webhook Support
  
---

# 🖥 Dashboard Preview

## Main Dashboard

<img src="images/dashboard.png"/>

---

## Threat Detection

<img src="images/alerts.png"/>

---

## Live Monitoring

<img src="images/resources.png"/>

---

# ⚙️ Installation

```bash
git clone https://github.com/webixly/Netguard-V2.git

cd Netguard-V2

pip install -r requirements.txt
```

---

# 🚀 Usage

```bash
python netguard.py --watch sample.log
```

or

```bash
python netguard.py --watch /var/log/auth.log
```

---

# 📂 Project Structure

```
Netguard-V2/

│

├── core/

│ ├── log_watcher.py

│ ├── monitor.py

│ └── scanner.py

│

├── ui/

│ └── display.py

│

├── images/

├── requirements.txt

├── sample.log

└── netguard.py
```

---

# ⚡ Detection Engine

NetGuard V2 continuously analyzes log streams using a high-performance regex engine capable of identifying:

| Category | Detection |
|----------|-----------|
| Authentication | Brute Force |
| Web | SQLi |
| Web | XSS |
| Web | Directory Traversal |
| Malware | Web Shell |
| Exploitation | RCE |
| Reconnaissance | Nmap |
| Network | Port Scan |
| Infrastructure | DoS |
| Malware | Crypto Mining |

---

# 🌍 Real-World Use Cases

✔ Linux Servers

✔ SOC Monitoring

✔ Blue Team Operations

✔ Home Labs

✔ VPS Monitoring

✔ Security Training

---

# 📈 Roadmap

- [x] Threat Detection
- [x] Resource Monitoring
- [x] Discord Alerts
- [ ] IP Auto Blocking
- [ ] Email Notifications
- [ ] Web Dashboard
- [ ] Multi-Log Monitoring
- [ ] AI Threat Classification

---

# 🛠 Tech Stack

- Python
- Rich
- Psutil
- Requests
- Regex
- Linux Logs

---

# 👨‍💻 Author

### Ayman

Blue Team • Infrastructure Security • Python Developer

GitHub:

https://github.com/webixly

---

<div align="center">

⭐ Star the project if you find it useful.

</div>
