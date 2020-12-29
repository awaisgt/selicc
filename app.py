import requests
import smtplib
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

link_type = 'https://www.daraz.pk/products/buy-1-get-1-free-blutooth-handfree-wireless-bluetooth-headset-good-quality-bluetooth-handsfree-earphone-i143850138-s1305074376.html?spm=a2a0e.home.flashSale.4.35e34937DPyUTh&search=1&mp=1&c=fs'

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("awaisghbh@gmail.com", "pakarmy123")
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
while(True):
	if ("daraz" or "DARAZ") in link_type :
		driver.get(link_type)
		price = driver.find_elements_by_class_name("pdp-price")[0]
		price_int = float(price.text[4:])
		message =str(price_int)
		s.sendmail("awaisghbh@gmail.com", "awaisghaffar77@gmail.com", message)
		s.quit()
		print("ok")
		time.sleep(50)
		print("ok")
		time.sleep(50)
		print("ok")
		time.sleep(50)
		print("ok")
		time.sleep(50)
		print("ok")
		time.sleep(50)

if ("amazon" or "AMAZON") in link_type :
	driver.get(link_type)
	price = driver.find_element_by_id("priceblock_ourprice")
	price_int = float(price.text[1:])
