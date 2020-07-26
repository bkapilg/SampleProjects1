import time
#from selenium.webdriver import Chrome
from selenium import webdriver
print()
driver = webdriver.Chrome("C:\\Users\\20126635\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.back()
driver.refresh()
time.sleep(50)
driver.close()
