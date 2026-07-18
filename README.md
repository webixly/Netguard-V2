<div align="center">

# 🛡️ NetGuard V2

### Advanced Infrastructure Security Dashboard

Enterprise-grade Blue Team tool for monitoring Linux servers, detecting security threats, and visualizing system health in real-time.

<img src="images/dashboard.png" width="900"/>

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Linux-Supported-black?style=for-the-badge&logo=linux)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

</div>

---

# 📖 Overview

NetGuard V2 is an advanced Blue Team monitoring dashboard designed to detect suspicious activities from Linux log files while simultaneously monitoring server resources.

Unlike traditional log viewers, NetGuard V2 combines:

- 🔍 Threat Detection
- 📊 Live Infrastructure Monitoring
- 🚨 Instant Discord Alerts
- 🖥️ Rich Terminal Dashboard

into one lightweight terminal application.

---

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
