from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

driver.get("https://www.amazon.in/")
time.sleep(2)
driver.find_element_by_id("twotabsearchtextbox").send_keys("wrist watch")
time.sleep(2)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(1)
driver.find_element_by_partial_link_text("6,918").click()
time.sleep(5)

driver.close()
print("test case completed")