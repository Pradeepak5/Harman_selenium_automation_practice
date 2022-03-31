from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Facebook")
time.sleep(3)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys("8270748551")
driver.find_element_by_name("pass").send_keys("Pradeep@571")
driver.find_element_by_name("login").send_keys(Keys.ENTER)
time.sleep(10)

driver.close()

print("Test case Completed....")


