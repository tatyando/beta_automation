from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

for x in range(0,3):
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()