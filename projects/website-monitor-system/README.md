# Website Monitor System Design

## Overview
A comprehensive website monitoring system built with FastAPI, SQLite, supporting HTTP monitoring, email/SMS alerts, and a web dashboard.

## Technology Stack
- **Backend**: FastAPI (Python async web framework)
- **Database**: SQLite (file-based, no setup required)
- **Frontend**: HTML/CSS/JavaScript (FastAPI templates)
- **Email**: smtplib/scmtplib for email alerts
- **SMS**: twilio/twilio for SMS integration (optional)

## Core Components

### 1. Monitor Service
- **HTTP Checker**: Validates website availability, response codes, latency
- **Scheduler**: Background task runner using `asyncio` + `schedule`
- **Alert Engine**: Triggers notifications based on configurable rules
- **Data Collector**: Stores historical monitoring data

### 2. Database Schema
```sql
-- Websites to monitor
CREATE TABLE websites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    name TEXT NOT NULL,
    monitoring_enabled BOOLEAN DEFAULT 1,
    check_interval_seconds INTEGER DEFAULT 300,
    expected_status_code INTEGER DEFAULT 200,
    expected_response_time_ms INTEGER DEFAULT 5000,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Monitoring results
CREATE TABLE monitoring_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website_id INTEGER,
    status_code INTEGER,
    response_time_ms INTEGER,
    is_up BOOLEAN NOT NULL,
    error_message TEXT,
    checked_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (website_id) REFERENCES websites(id)
);

-- Alert configurations
CREATE TABLE alert_configs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website_id INTEGER,
    alert_type TEXT NOT NULL, -- 'email', 'sms'
    destination TEXT NOT NULL, -- email address or phone number
    notify_on_down BOOLEAN DEFAULT 1,
    notify_on_recovery BOOLEAN DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (website_id) REFERENCES websites(id)
);

-- Alert history
CREATE TABLE alerts_sent (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website_id INTEGER,
    alert_config_id INTEGER,
    alert_type TEXT NOT NULL,
    status TEXT NOT NULL, -- 'up' or 'down'
    message TEXT,
    sent_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (website_id) REFERENCES websites(id),
    FOREIGN KEY (alert_config_id) REFERENCES alert_configs(id)
);
```

### 3. Application Structure
```
website-monitor/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── database.py       # SQLite database connection
│   ├── models.py         # Pydantic models
│   ├── monitor.py        # Core monitoring logic
│   ├── alert.py          # Alert system
│   └── routers/
│       ├── dashboard.py  # Web dashboard
│       ├── api.py        # REST API endpoints
│       └── websites.py   # Website management
├── static/               # CSS, JS files
├── templates/            # Jinja2 templates
├── migrations/           # Database migrations
├── config.py             # Configuration
├── requirements.txt
└── README.md
```

## Monitoring Features

### HTTP Monitoring
- **Status Code Validation**: Check for expected HTTP response codes
- **Response Time Monitoring**: Track page load times
- **SSL Certificate Checking**: Warn about upcoming expirations
- **Content Validation**: Optional string matching in page content
- **Custom Headers**: Support for authentication/custom headers

### Alerting System
- **Email Alerts**: SMTP integration for notification emails
- **SMS Alerts**: Twilio integration for SMS notifications
- **Alert Rules**: Configurable conditions (down, slow response, recovery)
- **Cooldown Periods**: Prevent alert spam
- **Escalation Rules**: Progressive alert escalation

### Dashboard Features
- **Real-time Status**: Live monitoring results
- **Historical Charts**: Uptime and response time graphs
- **Incident Timeline**: Log of downtimes and recoveries
- **Bulk Management**: Add/edit multiple websites
- **Alert Configuration**: Manage alert settings

## API Endpoints

### Website Management
- `GET/POST /websites` - List and add websites
- `PUT/DELETE /websites/{id}` - Update or remove website
- `GET /websites/{id}/status` - Get current status
- `GET /websites/{id}/history` - Get monitoring history

### Alerts
- `GET/POST /alerts/recipients` - Manage alert recipients
- `DELETE /alerts/{id}` - Remove alert configuration

### Dashboard
- `GET /` - Main dashboard
- `GET /website/{id}` - Individual website details
- `GET /alerts` - Alert history and configuration

## Development Workflow

1. **Setup environment**:
   ```bash
   cd website-monitor
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Initialize database**:
   ```bash
   python -c "from app.database import init_db; init_db()"
   ```

3. **Run development server**:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Add websites to monitor**:
   - Use web interface at http://localhost:8000
   - Or use API directly

5. **Configure alerts**:
   - Add email/SMS destinations
   - Set alert conditions

## Configuration

Environment variables in `.env` file:
```
DATABASE_URL=sqlite:///./website_monitor.db
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_password

# Optional SMS (Twilio)
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_FROM_NUMBER=+1234567890

SECRET_KEY=your_secret_key
DEBUG=true
```

## Reliability Considerations

- **Error Handling**: Comprehensive exception handling
- **Retry Logic**: Automatic retries for transient failures
- **Rate Limiting**: Respect site robots.txt and rate limits
- **Resource Monitoring**: Monitor system resources (CPU, memory)
- **Logging**: Structured logging with different levels

## Future Enhancements

- Multi-region monitoring (check from different geographic locations)
- Advanced metrics (page size, compression, security headers)
- Integration with external monitoring services (statuspage.io, pingdom)
- Slack/Teams notifications
- API rate limiting and authentication
- Docker containerization
- Grafana/Prometheus integration