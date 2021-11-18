# import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

email = "admin@gmail.com"
password = "123456"
# site_url = "https://dev.txtred.com/"
site_url = "https://dev.txtred.com/"

# Chrome
driver = webdriver.Chrome("/home/studio45/Downloads/chromedriver_linux64/chromedriver")
# driver.maximize_window()
driver.get(site_url)
sleep(2)
driver.find_element(By.NAME, 'email').send_keys(email)
sleep(1)
driver.find_element(By.NAME, 'password').send_keys(password)
sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/div[4]/button").click()
sleep(3)
# driver.get("https://dev.txtred.com/dashboard/")
driver.get(site_url+"dashboard/")
sleep(3)
# driver.get("https://dev.txtred.com/user-moov/")
driver.get(site_url+"user-moov/")
sleep(2)
driver.find_element_by_id('id_type').click()
sleep(2)
sel = Select(driver.find_element_by_id("id_type"))
sel.select_by_value('Checking')
# sel.select_by_index(1)
sleep(2)
driver.find_element(By.NAME, 'checking_account_number').send_keys('464654644')
sleep(1)
driver.find_element(By.NAME, 'routing_number').send_keys('031176110')
sleep(1)
driver.find_element(By.NAME, 'confirm_routing_number').send_keys('031176110')
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/form/div[5]/button").click()
# driver.find_element(By.ID, 'moov_information').click()
sleep(10)

driver.close()
