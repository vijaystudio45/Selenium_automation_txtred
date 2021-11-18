# import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

# import Alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement

email = "admin@gmail.com"
password = "123456"
# site_url = "http://127.0.0.1:8000/"
site_url = "https://dev.txtred.com/"

# Chrome
driver = webdriver.Chrome("/home/studio45/Downloads/chromedriver_linux64/chromedriver")
driver.get(site_url)
sleep(2)
driver.find_element(By.NAME, 'email').send_keys(email)
sleep(1)
driver.find_element(By.NAME, 'password').send_keys(password)
sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[4]/button").click()
sleep(3)
driver.get(site_url+"dashboard/")
sleep(3)
driver.get(site_url+"manage-user-by-admin/")
sleep(3)
driver.get(site_url+"edit-user-by-admin/3/")
sleep(3)
driver.find_element(By.ID, 'id_moov_id').clear()
sleep(2)
driver.find_element(By.ID, 'id_moov_id').send_keys('27112000')
sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/form/div[11]/div[1]/button").click()
sleep(5)
driver.get(site_url+"manage-user-by-admin/")
sleep(4)
driver.close()
