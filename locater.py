from selenium import webdriver
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome("D:\\chromedriver_win32 (6)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_css_selector("input[name='name']").send_keys("bbb")
driver.find_element_by_id("exampleCheck1").click()
# Select class provide the methds to handle the option in dropdowndr
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)
driver.find_element_by_name("bday").send_keys("11/06/1995")
driver.find_element_by_name("email").send_keys("shetty")

driver.find_element_by_xpath("//input[@type='submit']").click()
#print (driver.find_element_by_class_name("alert-success").text)
# # //*[contains(@class, "alert-success')]   -xpath
# #[class*='alert-success']    -CSS
# driver = webdriver.Chrome("C:\\Users\\20126635\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
# driver.get("http://183.82.100.55/ranford1/home.aspx")
# driver.find_element_by_id("txtuId").send_keys("admin")
# driver.find_element_by_id("txtPword").send_keys("M1ndqLp")
# driver.find_element_by_id("login").click()
# driver.find_element_by_xpath()