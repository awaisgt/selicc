import requests
import smtplib
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("awaisghbh@gmail.com", os.environ.get("PASSWORD_HIDDEN"))
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
while(True):
	driver.get("http://flasktestk.herokuapp.com/show")
	link = driver.find_elements_by_class_name("username")[0]
	driver.get(link.text)
	price = driver.find_elements_by_class_name("pdp-price")[0]
	price_int = float(price.text[4:])
	message =str(price_int)
	s.sendmail("awaisghbh@gmail.com", "awaisghaffar77@gmail.com", message)
	s.quit()
	print("ok")
	time.sleep(20)
	print("ok")
	time.sleep(20)
	print("ok")
	time.sleep(20)
	print("ok")
	time.sleep(20)
	print("ok")
	time.sleep(20)
