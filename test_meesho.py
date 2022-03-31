from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("meesho")
time.sleep(3)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
driver.get("https://meesho.com/")
driver.find_elements_by_class_name("Text__StyledText-sc-oo0kvp-0 ZkhsR TextSearch__Input-sc-n7qqmw-2 hPATZW search-input-elm TextSearch__Input-sc-n7qqmw-2 hPATZW search-input-elm").send_keys("wrist watch")
driver.find_element_by_class_name("Icon-sc-1iwi4w1-0 hPstgX").send_keys(Keys.ENTER)
time.sleep(2)

driver.close()
print("Tested Successfully")