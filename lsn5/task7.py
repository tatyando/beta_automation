from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/inputs")

input = driver.find_element(By.CSS_SELECTOR, "input")
input.send_keys(1000)
input.clear()
input.send_keys("SkyPro")
