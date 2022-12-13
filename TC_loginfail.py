from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time

driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_users")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


Notif = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
print(Notif.text)

time.sleep(5)
driver.close()