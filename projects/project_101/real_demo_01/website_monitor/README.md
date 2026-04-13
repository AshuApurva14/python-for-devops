# 🌐 Website Availability Monitor (Python)

A lightweight, Python-based website monitoring system that continuously checks website availability, validates HTTP response codes, measures response times, logs uptime/downtime history, and triggers alerts on failure — built without any external monitoring infrastructure.

> **Core DevOps philosophy:** *Monitoring before failure becomes visible. Automation over manual checks. Observability starts small — not with tools.*

***

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Alerting](#alerting)
- [Scheduling with Cron](#scheduling-with-cron)
- [Logs & Reports](#logs--reports)
- [Concepts Covered](#concepts-covered)
- [Why This Project Matters](#why-this-project-matters)

***

## ✨ Features

- HTTP/HTTPS availability checks using Python's `requests` library
- Response code validation — 2xx (success), 4xx (client errors), 5xx (server errors)
- Response time measurement with configurable latency thresholds
- Persistent uptime/downtime history via structured JSON logging
- Alert mechanisms: email (SMTP), log file, and webhook (Slack/Discord)
- Cron-compatible CLI — fully automated with `crontab`
- Zero external monitoring tools — pure Python standard library + `requests`

***

## 📁 Project Structure

```
website-monitor/
├── monitor.py              # Core monitoring engine
├── alert.py                # Alert dispatcher (email / webhook / log)
├── report.py               # Daily uptime summary generator
├── config.yaml             # Target URLs, thresholds, alert settings
├── logs/
│   ├── uptime.log          # Full structured check history (JSON lines)
│   └── downtime.log        # Failure-only log for quick incident review
├── reports/
│   └── daily_summary.txt   # Generated daily uptime report
├── requirements.txt        # Python dependencies
└── README.md
```

***

## ⚙️ Prerequisites

- Python 3.8+
- pip

Install dependencies:

```bash
pip install -r requirements.txt
```

**`requirements.txt`:**
```
requests>=2.31.0
PyYAML>=6.0
```

***

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/website-monitor-python.git
cd website-monitor-python

# Install dependencies
pip install -r requirements.txt

# Edit config with your target URLs
nano config.yaml

# Run a manual check
python monitor.py

# Or run in verbose mode
python monitor.py --verbose
```

***

## 🔧 Configuration

Edit `config.yaml` to define monitoring targets and thresholds:

```yaml
targets:
  - url: "https://example.com"
    name: "Example Site"
    expected_status: 200
  - url: "https://yourdomain.com"
    name: "Production API"
    expected_status: 200

thresholds:
  response_time_seconds: 3.0   # Alert if response exceeds this
  timeout_seconds: 10          # Request timeout

alerting:
  method: "log"                # Options: "log" | "email" | "webhook"
  webhook_url: ""              # Slack or Discord webhook URL
  email:
    smtp_host: "smtp.gmail.com"
    smtp_port: 587
    sender: "monitor@yourdomain.com"
    password: ""               # Use env var: MONITOR_EMAIL_PASSWORD
    recipients:
      - "ops@yourdomain.com"

logging:
  uptime_log: "logs/uptime.log"
  downtime_log: "logs/downtime.log"
```

> **Security Tip:** Never hardcode credentials. Use environment variables or a `.env` file (excluded from `.gitignore`).

***

## 🔔 Alerting

The `alert.py` module supports three alert modes:

### Log Alert (default)

All failures are appended to `logs/downtime.log` in JSON Lines format.

```json
{"timestamp": "2026-04-13T23:00:01Z", "url": "https://example.com", "status": "DOWN", "http_code": 503, "response_time": null}
```

### Email Alert (SMTP)

Configure SMTP settings in `config.yaml`. Uses Python's built-in `smtplib`.

```yaml
alerting:
  method: "email"
  email:
    smtp_host: "smtp.gmail.com"
    smtp_port: 587
    sender: "monitor@yourdomain.com"
    password: "${MONITOR_EMAIL_PASSWORD}"
    recipients:
      - "you@yourdomain.com"
```

### Webhook Alert (Slack / Discord)

Sends a JSON `POST` payload via `requests` to your configured webhook URL.

```yaml
alerting:
  method: "webhook"
  webhook_url: "https://hooks.slack.com/services/XXX/YYY/ZZZ"
```

**Slack payload example (auto-generated):**
```json
{
  "text": "🚨 *ALERT*: https://example.com is DOWN | Status: 503 | Time: 2026-04-13 23:05:01 UTC"
}
```

***

## ⏰ Scheduling with Cron

Add a cron job to run checks automatically every 5 minutes:

```bash
crontab -e
```

```cron
# Website monitor — runs every 5 minutes
*/5 * * * * /usr/bin/python3 /path/to/website-monitor-python/monitor.py >> /path/to/website-monitor-python/logs/cron.log 2>&1

# Daily report — runs at midnight
0 0 * * * /usr/bin/python3 /path/to/website-monitor-python/report.py
```

> **Tip:** Use `which python3` to verify the Python path on your system.

***

## 📊 Logs & Reports

### Uptime Log (`logs/uptime.log`) — JSON Lines

```json
{"timestamp": "2026-04-13T23:00:01Z", "name": "Example Site", "url": "https://example.com", "status": "UP", "http_code": 200, "response_time_s": 0.342}
{"timestamp": "2026-04-13T23:05:01Z", "name": "Example Site", "url": "https://example.com", "status": "DOWN", "http_code": 503, "response_time_s": null}
```

### Downtime Log (`logs/downtime.log`)

Failure-only entries, same format — for rapid incident review and post-mortems.

### Daily Report (`report.py`)

Run `python report.py` to generate `reports/daily_summary.txt`:

```
============================================================
  Website Uptime Report — 2026-04-13
============================================================
 Site            | Uptime %  | Total Down | Incidents
 Example Site    | 99.30%    | ~4 min     | 1
 Production API  | 100.00%   | 0 sec      | 0
============================================================
```

***

## 📚 Concepts Covered

| Concept | Implementation |
|---|---|
| HTTP request lifecycle | `requests.get()` with timeout and response parsing |
| HTTP status codes | Conditional checks on `response.status_code` (2xx/4xx/5xx) |
| Response time measurement | `time.perf_counter()` around HTTP request |
| Failure detection logic | Threshold-based: status code mismatch OR latency breach |
| Structured logging | JSON Lines format for machine-readable uptime history |
| Alert dispatching | Pluggable `alert.py` module — log / SMTP / webhook |
| Cron scheduling | CLI-compatible `monitor.py` invoked via crontab |
| Report generation | `report.py` reads logs and calculates uptime percentages |
| Config management | Externalized YAML config, env vars for secrets |

***

## 🧠 Why This Project Matters

This project embodies core **SRE and DevOps thinking**:

- **Proactive monitoring** — detect outages before users report them
- **Automation over manual** — eliminate repetitive health checks
- **Structured logging** — machine-readable JSON logs make this grep-friendly and pipeline-ready
- **Observability at scale starts small** — before Prometheus and Grafana, understand *why* you need them

This is the mental model behind every production monitoring system, implemented from scratch.

***

## 🗺️ Extension Ideas

Once the core is working, extend it:

- [ ] Add SSL certificate expiry checks (`ssl`, `datetime`)
- [ ] Track DNS resolution time separately
- [ ] Store logs in SQLite for richer querying
- [ ] Add a Flask/FastAPI dashboard to visualize uptime history
- [ ] Implement exponential backoff before alerting (reduce flapping alerts)
- [ ] Dockerize and deploy as a persistent background service
- [ ] Export metrics to Prometheus via `/metrics` endpoint

***

## 📄 License

MIT License — free to use, modify, and distribute.