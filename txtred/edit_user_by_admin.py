# import self as self
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

# import Alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement

email = "admin@gmail.com"
password = "123456"
site_url = "https://dev.txtred.com/"
# site_url = "http://127.0.0.1:8000/"

# Chrome
driver = webdriver.Chrome("/home/studio45/Downloads/chromedriver_linux64/chromedriver")
driver.get(site_url)
sleep(2)
driver.find_element(By.NAME, 'email').send_keys(email)
driver.find_element(By.NAME, 'password').send_keys(password)
sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[4]/button").click()
sleep(3)
# driver.get("https://dev.txtred.com/dashboard/")
driver.get(site_url+"dashboard/")
sleep(3)
# driver.get("https://dev.txtred.com/edit-user-profile/")
driver.get(site_url+"edit-user-profile/")
sleep(3)
# clears the content
# driver.find_element(By.NAME, 'address_1').clear()
driver.find_element_by_id('id_address_1').clear()
sleep(2)

# randstring = ''.join(random.choices(string.ascii_uppercase, k=8))
randstring = ''.join(random.choices(string.ascii_lowercase, k=8))
# randstring = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
# element.send_keys(randstring)

# driver.find_element(By.NAME, 'address_1').send_keys('Chandigarh')
driver.find_element(By.NAME, 'address_1').send_keys(randstring)
sleep(2)
driver.find_element(By.ID, 'id_tin_matched_date').clear()
sleep(2)
driver.find_element(By.ID, 'id_tin_matched_date').send_keys('27/11/2000')
# driver.find_element(By.ID, 'id_tin_matched_date').click()
sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/form/div[10]/button").click()
sleep(3)
# driver.get("https://dev.txtred.com/edit-user-profile/")
driver.get(site_url+"edit-user-profile/")
sleep(3)
driver.close()
