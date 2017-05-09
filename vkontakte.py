from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\\ustanovka\\chromedriver_win32\\chromedriver.exe")
driver.get("https://vk.com")
username = driver.find_element_by_id('index_email')
username.clear()
username.send_keys("izm-zubko@yandex.ru")
password = driver.find_element_by_id('index_pass')
password.clear()
password.send_keys("starkiller13063")
password.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

