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

backpack = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
print(backpack.text)
time.sleep(1)

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()
time.sleep(1)

assert driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span")
time.sleep(1)

backpack = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
print(backpack.text)
time.sleep(1)

time.sleep(5)
driver.close()







 