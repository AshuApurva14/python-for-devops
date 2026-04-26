import requests
import logging
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from requests.exceptions import HTTPError



logging.basicConfig(
    filename='website_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Check the HTTP response
def check_website_response(URL):
    

        try:

           response = requests.get(URL, timeout=5)
           if response.status_code == 200 or response.status_code == 304:
              logging.info(f"UP:{URL} is online")
           else:
              msg =  f"DOWN: {URL} returned status code {response.status_code}"
              logging.warning(msg)
              send_alert_messgae("Website Down Alert", msg)

        except HTTPError as http_err:
            msg = f"DOWN: {URL} is unreachable. {http_err}"
            logging.error(msg)
            send_alert_messgae("Website  unreachable aler", msg)
    
def send_alert_messgae(subject, body):
    

    try:
        # Email Configurations
        EMAIL_SENDER = "aapurva74@gmail.com"
        EMAIL_RECIEVER = "devopsdre5@gmail.com"
        EMAIL_PASSWORD = "Your password"
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 465

        msg = MIMEText(body)
        msg['Subject'] = f"Website Monitor Status:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECIEVER

        with smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        logging.info("Email alert sent successfully")

    except Exception as e:
        logging.error(f"Failed to send alert {e}")


URL = "https://www.google.com"
INTERVAL = 60

if __name__ == "__main__":
    print(f"Monitoring Started for {URL} ...., Please Wait!")
    while True:
     
     check_website_response(URL)
     time.sleep(INTERVAL)
    
