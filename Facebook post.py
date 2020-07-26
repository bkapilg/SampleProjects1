from selenium import webdriver
from time import sleep
import time
#driver=webdriver.chrome("D:\Selenium software\chromedriver_win32")
driver =webdriver.Chrome("D:\\chromedriver_win32 (5)\\chromedriver.exe")
# Step 2) Navigate to Facebook
driver.get("http://www.facebook.com")
driver.find_element_by_id("email").send_keys("11mayank")
driver.find_element_by_id("pass").send_keys("Abc@24546")
driver.find_element_by_id("loginbutton").click()
# Step 3) Search & Enter the Email or Phone field & Enter Password
# username = driver.find_element_by_id("email")
# password = driver.find_element_by_id("pass")
# submit   = driver.find_element_by_id("loginbutton")
# username.send_keys("11mayank")
# password.send_keys("fkkffkfk")
# # Step 4) Click Login
# submit.click()
# sleep(13)
#
# alert = driver.switch_to.alert.accept()
# print(alert.text)
# alert.accept()
#
#
# postarea=driver.find_element_by_class_name("_5qtp")
# postarea.click()
# sleep(3)
#
# #activatepostarea=driver.switch_to_active_element()
# #acivepostarea=('Hello programmer')