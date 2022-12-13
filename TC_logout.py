from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time

driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

assert driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span")
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
time.sleep(1)

driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(1)

assert driver.find_element(By.ID, "login-button")

time.sleep(5)
driver.close()
