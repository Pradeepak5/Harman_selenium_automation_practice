from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

driver.get("https://www.w3schools.com/")
driver.find_element_by_link_text("Tutorials").click()
time.sleep(2)
driver.find_element_by_link_text("Learn Python").click()
time.sleep(2)
driver.find_element_by_link_text("Python MySQL Tutorial").click()
time.sleep(4)
driver.close()