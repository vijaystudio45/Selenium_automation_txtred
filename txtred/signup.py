from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
import time

# import Alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement

signup_userName = "Mohit"
signup_email = "mohit@gmail.com"
signup_password = "123456"

site_url = "https://dev.txtred.com/"
# site_url = "http://127.0.0.1:8000/"

# Chrome
driver = webdriver.Chrome("/home/studio45/Downloads/chromedriver_linux64/chromedriver")
driver.get(site_url)
sleep(2)
driver.find_element(By.ID, "m_login_signup").click()
sleep(2)
driver.find_element(By.NAME, 'username').clear()
sleep(1)
# userNames = ["Mandeep", "Tarsem", "Tushar", "Mohit", "Akshay", "Abinash"]
# randomUserName = random.choice(userNames)
# driver.find_element(By.NAME, 'username').send_keys(randomUserName)
driver.find_element(By.NAME, 'username').send_keys(signup_userName)
sleep(1)
driver.find_element(By.NAME, 'first_name').send_keys("Mandeep")
sleep(1)
driver.find_element(By.NAME, 'last_name').send_keys("Saini")
sleep(1)
# userEmails = ["mandeep@gmail.com", "tarsem@gmail.com", "tushar@gmail.com", "mohit@gmail.com", "akshay@gmail.com", "abinash@gmail.com"]
# randomUserEmail = random.choice(userEmails)
# driver.find_element(By.ID, 'id_email').send_keys(randomUserEmail)
driver.find_element(By.ID, 'id_email').send_keys(signup_email)
sleep(1)
driver.find_element(By.ID, 'id_password').clear()
sleep(1)
driver.find_element(By.ID, 'id_password').send_keys(signup_password)
sleep(1)
driver.find_element(By.ID, 'id_confirm_password').send_keys("123456")
sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[3]/form/div[4]/div/label").click()
sleep(1)
driver.find_element(By.ID, 'm_login_signup_submit').click()  ### SignUp Button
# driver.get("https://dev.txtred.com/dashboard/")
# driver.get(site_url+"dashboard/")
sleep(3)
# print(driver.current_url)
# msg = driver.switchTo().alert().getText()
# driver.switchTo().alert().getText()
# print(msg)
sleep(5)
driver.find_element(By.NAME, 'email').send_keys(signup_email)
driver.find_element(By.NAME, 'password').send_keys(signup_password)
sleep(1)
driver.find_element(By.ID, "m_login_signin_submit").click()
sleep(12)

driver.find_element(By.ID, 'id_ssn').send_keys("123-45-6789")
sleep(1)
driver.find_element(By.ID, 'id_phone_number').send_keys("+918708245955")
sleep(1)
driver.find_element(By.ID, 'id_suffix').send_keys("Sr")
sleep(1)
driver.find_element(By.ID, 'id_address_1').send_keys("Hotel Staybridge")
sleep(1)
driver.find_element(By.ID, 'id_address_2').send_keys("Crooke Street")
sleep(1)
driver.find_element(By.ID, 'id_city').send_keys("San Jose")
sleep(1)
driver.find_element(By.ID, 'id_state').click()
sleep(1)
driver.find_element(By.ID, 'id_state').click()
# b.find_element_by_xpath("//select[@name='element_name']/option[text()='option_text']").click()
driver.find_element_by_xpath("//select[@name='state']/option[text()='California']").click()
sleep(1)
driver.find_element(By.ID, 'id_zipcode').send_keys("95124-1003")
sleep(1)
driver.find_element(By.ID, "id_accept_contract").click()
sleep(1)
# driver.find_element(By.ID, 'personal_information').click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[10]/button").click()
sleep(15)


driver.close()
