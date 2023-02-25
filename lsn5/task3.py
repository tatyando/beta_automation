from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_element_locator = '[onclick="addElement()"]'
add_element_button = driver.find_element(By.CSS_SELECTOR, add_element_locator)

for x in range (0,5): 
    add_element_button.click()

delete_buttons = driver.find_elements(By.CSS_SELECTOR, '.added-manually')
print(len(delete_buttons))
