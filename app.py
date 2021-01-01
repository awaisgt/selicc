import requests
import smtplib
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
def send_email(price,link):
	from email.mime.text import MIMEText
	from email.mime.application import MIMEApplication
	from email.mime.multipart import MIMEMultipart
	from smtplib import SMTP
	import smtplib
	import sys
	recipients = ['awaisghaffar77@gmail.com'] 
	emaillist = [elem.strip().split(',') for elem in recipients]
	msg = MIMEMultipart()
	msg['Subject'] = "pppppppppp" 
	msg['From'] = "anything"

	html = f"""\
		<!DOCTYPE html>
<html>
<head>

</head>
<body>

<table id="customers" style = " border-collapse: collapse;
  width: 100%;">
  <tr style = " padding-top: 25px; padding-bottom: 25px; background-color: #f2f2f2;" >
    <th style = "  padding: 15px;padding-top: 25px;padding-bottom: 25px; text-align: left; background-color: #008891; color: white;   ">Product</th>
    <th style = "  padding: 15px;padding-top: 25px;padding-bottom: 25px; text-align: left; background-color: #008891; color: white;   " >Price</th>
    <th style = "  padding: 15px;padding-top: 25px;padding-bottom: 25px; text-align: left; background-color: #008891; color: white;   " >Link</th>
  </tr>
  <tr style = " padding-top: 25px; padding-bottom: 25px; background-color: #f2f2f2;" >
    <td style = "padding: 15px; padding-top: 25px; padding-bottom: 25px; ">Alfreds Futterkiste</td>
    <td style = "padding: 15px; padding-top: 25px; padding-bottom: 25px; ">{{price}}</td>
    <td style = "padding: 15px; padding-top: 25px; padding-bottom: 25px; ">{{link}}</td>
  </tr>
  
</table>

</body>
</html>"""

	part1 = MIMEText(html, 'html')
	msg.attach(part1)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('awaisghbh@gmail.com', os.environ.get("PASSWORD_HIDDEN"))
	server.sendmail(msg['From'], emaillist, msg.as_string())
	server.close()
	
	
	
	
	

#s = smtplib.SMTP('smtp.gmail.com', 587)
#s.starttls()
#s.login("awaisghbh@gmail.com", os.environ.get("PASSWORD_HIDDEN"))
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
while(True):
	driver.get("http://flasktestk.herokuapp.com/show")
	link = driver.find_elements_by_class_name("username")[0]
	temp = link.text
	driver.get(link.text)
	price = driver.find_elements_by_class_name("pdp-price")[0]
	price_int = float(price.text[4:])
	message =str(price_int)
	send_email(price_int,temp)
	#s.sendmail("awaisghbh@gmail.com", "awaisghaffar77@gmail.com", message)
	#s.quit()
	print("ok")
	time.sleep(300)
