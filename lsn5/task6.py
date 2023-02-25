from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(3)
driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()
