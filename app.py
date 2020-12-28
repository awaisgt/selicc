import requests
import smtplib
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

link_type = 'https://www.daraz.pk/products/u1-handfree-high-bass-good-quality-good-sound-i128273142-s1287257140.html?spm=a2a0e.home.flashSale.3.35e349379B5Wi4&search=1&mp=1&c=fs'


if ("daraz" or "DARAZ") in link_type :
	#daraz link
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
  	chrome_options.add_argument("--headless")
  	chrome_options.add_argument("--disable-dev-shm-usage")
  	chrome_options.add_argument("--no-sandbox")
  	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
	driver.get(link_type)
	price = driver.find_elements_by_class_name("pdp-price")[0]
	price_int = float(price.text[4:])
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("awaisghbh@gmail.com", "pakarmy123")
	message =str(price_int)
	s.sendmail("awaisghbh@gmail.com", "awaisghaffar77@gmail.com", message)
	s.quit()

if ("amazon" or "AMAZON") in link_type :
	#daraz link
	chrome_options = webdriver.ChromeOptions()
  	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
  	chrome_options.add_argument("--headless")
  	chrome_options.add_argument("--disable-dev-shm-usage")
  	chrome_options.add_argument("--no-sandbox")
  	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
	driver.get(link_type)
	price = driver.find_element_by_id("priceblock_ourprice")
	price_int = float(price.text[1:])

	
