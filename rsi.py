import yfinance as yf
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ta.momentum import RSIIndicator
from datetime import datetime
from tabulate import tabulate

# --- Config ---
STOCK_SYMBOL = "INFY.NS"
RSI_PERIOD = 14
EMAIL_SENDER = "dsgurushantha@gmail.com"
EMAIL_RECEIVER = "dsgurushanthahuf@gmail.com"
EMAIL_PASSWORD = "ueerezshqkhjrovh"
sheet_id = "13l4k-GYe_L1SGabCvI0pcUxnYO_IJdGuye9Z8aQS0AI"


# --- Send Email ---
def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = subject
    msg.attach(MIMEText(html_body, 'html'))
    # msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

# --- Main ---
if __name__ == "__main__":
  today = datetime.today().strftime("%Y-%m-%d")
  subject = f"RSI Report - {today}"
  # body = f"The EMA for report on {ema_data} on {latest_date}."
  df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
  html_table = df.to_html(index=False)

  html_body = f"""
  <html>
    <body>
      <p>Hello,<br><br>
        Please find the data below:<br><br>
        {html_table}
      </p>
    </body>
  </html>
  """
  # text = text.format(table=tabulate(data1, headers="firstrow", tablefmt="grid"))
  send_email(subject, html_body)
