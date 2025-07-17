import yfinance as yf
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ta.momentum import RSIIndicator
from datetime import datetime
from tabulate import tabulate
import time

# --- Config ---
STOCK_SYMBOL = "INFY.NS"
RSI_PERIOD = 14
EMAIL_SENDER = "dsgurushantha@gmail.com"
EMAIL_RECEIVER = "dsgurushanthahuf@gmail.com"
EMAIL_PASSWORD = "ueerezshqkhjrovh"
gsheet_id = "13l4k-GYe_L1SGabCvI0pcUxnYO_IJdGuye9Z8aQS0AI"
sheet_name = 'Final List for RSI'

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

#import pandas as pd

# Replace with your actual Sheet ID and Sheet Name
#gsheet_id = '1Ts0kxeRk2MW6FsgZE4e9sG8XDxKSpl7VjCfgbct0n4g'
#sheet_

# Construct the URL for CSV export
  url = f'https://docs.google.com/spreadsheets/d/{gsheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

# Read the data into a Pandas DataFrame
  df = pd.read_csv(url)

# Print the DataFrame to verify
  print(df)

  # body = f"The EMA for report on {ema_data} on {latest_date}."
  #df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
  time.sleep(5)
  html_table = df.to_html(index=False)
  time.sleep(5)  
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
