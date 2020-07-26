from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\20126635\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")

driver.get("http://183.82.100.55/ranford1/home.aspx")
time.sleep(3)
driver.maximize_window()
driver.find_element_by_css_selector("#username").send_keys("rahul")
time.sleep(5)
driver.find_element_by_css_selector(".password").send_keys("sheety")
time.sleep(2)
#driver.find_element_by_css_selector(".password").clear()
# driver.find_element_by_link_text("Forgot Your Password?").click()
#driver.find_element_by_xpath("//a[text()='Cancel']").click()
##driver.find_element_by_xpath("//input[@type='submit']").click()    ("//a[text()='Cancel']")
# driver.find_element_by_xpath("//form[name='Login']//div[1]//label").text()
driver.find_element_by_id("Login").click()
