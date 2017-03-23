from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get('https://chime.me/')

driver.find_element_by_class_name("login").click()
sleep(2)
driver.find_element_by_name("email").send_keys("xiaoxue.wang@renren-inc.com")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_id("confirm-log").click()


