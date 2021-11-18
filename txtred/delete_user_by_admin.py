import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

email = "admin@gmail.com"
password = "123456"
site_url = "https://dev.txtred.com/"
# site_url = "http://127.0.0.1:8000/"

# Chrome
driver = webdriver.Chrome("/home/studio45/Downloads/chromedriver_linux64/chromedriver")
driver.get(site_url)
sleep(2)
driver.find_element(By.NAME, 'email').send_keys(email)
sleep(1)
driver.find_element(By.NAME, 'password').send_keys(password)
sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[4]/button").click()
sleep(5)
# driver.get("http://127.0.0.1:8000/manage-user-by-admin/")
driver.get(site_url+"manage-user-by-admin/")
sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/span/button").click()
sleep(3)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div[2]/button").click()
sleep(7)
# driver.execute_script("""
#    var l = document.getElementsByClassName("tp-logo")[0];
#    l.parentNode.removeChild(l);
# """)
driver.close()