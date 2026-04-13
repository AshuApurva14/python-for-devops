---
title: Website Availability Monitor
description: A lightweight Python-based website monitoring system built for DevOps engineers.
---

# 🌐 Website Availability Monitor

A lightweight, **Python-based** website monitoring system that continuously checks website
availability, validates HTTP response codes, measures response times, logs uptime/downtime
history, and triggers alerts on failure — built without any external monitoring infrastructure.

> **Core DevOps philosophy:** *Monitoring before failure becomes visible.
> Automation over manual checks. Observability starts small — not with tools.*

---

## 🚀 What Does It Do?

| Check | How |
|---|---|
| HTTP/HTTPS availability | `requests.get()` with configurable timeout |
| Response code validation | 2xx (success), 4xx (client error), 5xx (server error) |
| Response time measurement | `time.perf_counter()` around each request |
| Uptime/downtime logging | JSON Lines format — grep-friendly and pipeline-ready |
| Alert on failure | Log file, SMTP email, or Slack/Discord webhook |
| Scheduled automation | Cron-compatible CLI — runs every N minutes |

---

## 📁 Project Structure

```
website-monitor/
├── monitor.py # Core monitoring engine
├── alert.py # Alert dispatcher (email / webhook / log)
├── report.py # Daily uptime summary generator
├── config.yaml # Target URLs, thresholds, alert settings
├── logs/
│ ├── uptime.log # Full structured check history (JSON lines)
│ └── downtime.log # Failure-only log for quick incident review
├── reports/
│ └── daily_summary.txt # Generated daily uptime report
├── requirements.txt
└── README.md

```


---

## ⚡ Quick Start

**1. Clone the repository**

```bash
git clone https://github.com/your-username/website-monitor-python.git
cd website-monitor-python
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Add your target URLs in `config.yaml`**

```yaml
targets:
  - url: "https://example.com"
    name: "Example Site"
    expected_status: 200
```

**4. Run your first check**

```bash
python monitor.py --verbose
```

That's it! You will see output like:

```
[2026-04-13 23:00:01] ✅ UP | Example Site | Status: 200 | Time: 0.342s
[2026-04-13 23:00:02] 🚨 DOWN | Production API | Status: 503 | Time: N/A
```


---

## 🔔 Alert Modes

Choose one of three alerting methods in `config.yaml`:

- **`log`** — Write failures to `logs/downtime.log` (default, zero setup)
- **`email`** — Send SMTP alert via Python's built-in `smtplib`
- **`webhook`** — POST a JSON payload to Slack or Discord

See the [Alerting](alerting/log.md) section for full configuration details.

---

## ⏰ Automate with Cron

Run checks every 5 minutes without lifting a finger:

```cron
*/5 * * * * /usr/bin/python3 /path/to/monitor.py >> logs/cron.log 2>&1
```

See [Scheduling with Cron](scheduling/cron.md) for step-by-step setup.

---

## 🧠 Why This Project Matters

This project is not just a monitoring script — it is a hands-on introduction to
**SRE and DevOps thinking**:

- **Proactive monitoring** — detect outages before users report them
- **Automation over manual** — eliminate repetitive health checks
- **Structured logging** — JSON Lines logs are machine-readable and
  compatible with ELK, Loki, and Prometheus pipelines
- **Observability at scale starts small** — before Prometheus and Grafana,
  understand *why* you need them

---

## 🗺️ Extension Ideas

Once the core is working, extend the project further:

- [ ] SSL certificate expiry checks (`ssl`, `datetime`)
- [ ] DNS resolution time tracking
- [ ] SQLite backend for richer log querying
- [ ] Flask/FastAPI dashboard to visualize uptime history
- [ ] Exponential backoff before alerting (reduce flapping)
- [ ] Dockerize and deploy as a persistent background service
- [ ] Export metrics to Prometheus via a `/metrics` endpoint

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*Built with ❤️ by [Ashutosh Apurva](https://github.com/AshuApurva14)*