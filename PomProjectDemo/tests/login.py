from selenium import webdriver
import time
import calendar
import pytest
from pprint import pprint
import pdfkit
import unittest
import wkhtmltopdf
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys

from PomProjectDemo.pages.homePage import Homepage
from PomProjectDemo.pages.loginPage import LoginPage
from selenium.webdriver.support.ui import Select


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # def test_b_verify_succesfull_login(self):
    #     message = self.driver.find_element_by_id("welcome").text
    #     self.assertEqual(message, "Welcome Admin")
    #     print("Login Validation has been done")
    #
    # def test_a_first_login_valid(self):
    #     driver = self.driver
    #     driver.get("https://opensource-demo.orangehrmlive.com/")
    #     login = LoginPage(driver)
    #     login.enter_username("Admin")
    #     login.enter_password("admin123")
    #     login.click_login()
    #     self.driver.save_screenshot("C:\\Users\\20126635\\PycharmProjects\\untitled\\Screenshot\\login.png")
    #     print("Login successfull")
    #     time.sleep(5)
    #
    # def test_c_about(self):
    #     homepage = Homepage(self.driver)
    #     homepage.click_welcome()
    #     time.sleep(4)
    #     self.driver.find_element_by_link_text("About").click()
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('//*[@id="displayAbout"]/div/a').click()
    #     time.sleep(10)
    #     print ("Navigate to about")
    #
    # def test_d_logout(self):
    #     time.sleep(2)
    #     self.driver.find_element_by_link_text("Logout").click()
    #     print("logout successfully")
    #
    #
    # def test_e_second_login_invalid_Password(self):
    #     driver = self.driver
    #     driver.get("https://opensource-demo.orangehrmlive.com/")
    #     login = LoginPage(driver)
    #     login.enter_username("Admin")
    #     login.enter_password("admin156")
    #     login.click_login()
    #     message = driver.find_element_by_id("spanMessage").text
    #     self.assertEqual(message, "Invalid credentials")
    #     print("invalid Password")
    #
    # def test_f_third_invalid_username(self):
    #     driver = self.driver
    #     driver.get("https://opensource-demo.orangehrmlive.com/")
    #     login = LoginPage(driver)
    #     login.enter_username("abc")
    #     login.enter_password("admin123")
    #     login.click_login()
    #     message = driver.find_element_by_id("spanMessage").text
    #     self.assertEqual(message, "Invalid credentials")
    #     print("invalid Username")
    # def test_g_fourth_invalid_username_password(self):
    #     driver = self.driver
    #     driver.get("https://opensource-demo.orangehrmlive.com/")
    #     login = LoginPage(driver)
    #     time.sleep(4)
    #     login.enter_username("abc")
    #     login.enter_password("admin321")
    #     login.click_login()
    #     message = driver.find_element_by_id("spanMessage").text
    #     self.assertEqual(message, "Invalid credentials")
    #     print("invalid Username and Password")
    #     time.sleep(10)

    # # @pytest.mark.run(order=5)
    # def test_h_fifth_Forget_your_Password(self):
    #     self.driver.find_element_by_partial_link_text('Forgot').click()
    #     time.sleep(10)
    #     self.driver.find_element_by_id("securityAuthentication_userName").send_keys("Admin")
    #     self.driver.find_element_by_id("btnSearchValues").click()
    #     print("Forgot password successfully")

    # @pytest.mark.run(order=6)
    def test_j_sixth_cancel_button(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/requestPasswordResetCode")
        time.sleep(5)
        self.driver.find_element_by_id("btnCancel").click()  # TC_6
        print("Cancel clicked successfully")

    def test_k_Assign_leave(self):
        driver = self.driver
        login = LoginPage(driver)
        time.sleep(4)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[1]/div/a/span').click()
        print("Navigate to assign leave")

    def test_l_Enter_fields(self):
        self.driver.find_element_by_id("assignleave_txtEmployee_empName").send_keys("john smith")
        time.sleep(5)
        obj = Select(self.driver.find_element_by_id('assignleave_txtLeaveType'))
        obj.select_by_index('3')
        time.sleep(2)
        fromdate = self.driver.find_element_by_id("assignleave_txtFromDate")
        fromdate.clear()
        fromdate.send_keys("2020-04-02")
        fromdate.send_keys(Keys.ENTER)
        time.sleep(2)
        todate = self.driver.find_element_by_id("assignleave_txtToDate")
        todate.clear()
        todate.send_keys("2020-04-03")
        todate.send_keys(Keys.ENTER)
        time.sleep(3)
        obj1 = Select(self.driver.find_element_by_id('assignleave_partialDays'))
        obj1.select_by_index('3')
        self.driver.find_element_by_id("assignleave_txtComment").send_keys("No")
        self.driver.find_element_by_id("assignBtn").click()

    def test_m_Cancel_button(self):
        time.sleep(4)
        self.driver.find_element_by_id("confirmCancelButton").click()
        time.sleep(4)

    def test_n_Assign_button(self):
        self.driver.find_element_by_id("assignBtn").click()
        self.driver.find_element_by_id("confirmOkButton").click()
        time.sleep(3)
        self.driver.find_element_by_id("menu_leave_viewLeaveList").click()
        fromdate = self.driver.find_element_by_id("calFromDate")
        fromdate.clear()
        fromdate.send_keys("2020-04-02")
        fromdate.send_keys(Keys.ENTER)
        time.sleep(2)
        todate = self.driver.find_element_by_id("calToDate")
        todate.clear()
        todate.send_keys("2020-04-03")
        todate.send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element_by_id("leaveList_chkSearchFilter_checkboxgroup_allcheck").click()
        self.driver.find_element_by_id("leaveList_txtEmployee_empName").send_keys("john smith")
        self.driver.find_element_by_id("leaveList_cmbSubunit")
        self.driver.find_element_by_id("leaveList_cmbWithTerminated").click()

    def test_o_Search_button(self):
        self.driver.find_element_by_id("btnSearch").click()

    def test_p_personal_details(self):
        self.driver.find_element_by_link_text("John Smith").click()
        time.sleep(5)
        # message = self.driver.find_element_by_id("personal_txtEmpFirstName").text
        # self.assertEqual(message, "John")
        print("get by id successfull")

    def test_q_Edit_button(self):
        self.driver.find_element_by_xpath('//*[@id="btnSave"]').click()
        time.sleep(3)

    def test_r_Save_button(self):
        licence = self.driver.find_element_by_name("personal[txtLicenNo]").send_keys("123456")
        self.driver.find_element_by_id("btnSave").click()
        print("successfully saved")
        time.sleep(4)

    def test_s_Directory(self):
        self.driver.find_element_by_link_text("Directory").click()
        time.sleep(2)
        self.driver.find_element_by_id("searchDirectory_emp_name_empName").send_keys("John Smith")
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(3)
        self.driver.find_element_by_id("resetBtn").click()
        time.sleep(4)

    # def test_t_Dashboard(self):
    #     self.driver.find_element_by_id("Dashboard").click()

        # c = calendar.TextCalendar(calendar.SUNDAY)
        # str = c.formatmonth(2020, 1)
        # print (str)





     # # @pytest.mark.run(order=7)
        # message = self.driver.find_element_by_id("welcome").text  # TC_07
        # self.assertEqual(message, "Welcome Admin")
        # self.driver.find_element_by_id("displayAbout").click  # TC08
        # time.sleep(2)

        #  @pytest.mark.run(order=9)
        #  login = LoginPage(driver)
        #   sel.driver.find_element_by_id("logout").click  #TC09
        #  time.sleep(4)
        # @pytest.mark.run(order=10)
        # # login.enter_username("abc")
        # # login.enter_password("admin321")
        # # login.click_login()
        # # self.driver.find_element_by_class("quickLinkText").click() #TC10

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     print("test complete")


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\20126635\\PycharmProjects\\untitled\\Reports'))

    pdfkit.from_url('output', 'C:\\Users\\20126635\\PycharmProjects\\untitled\\Reports\\my_testpdf.pdf')
    # config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    #
    # pdfkit.from_url("http://google.com", "out.pdf", configuration=config)

   # pdfkit.from_file('C:\\Users\\20126635\\PycharmProjects\\untitled\\Reports\\TestResults___main__.LoginTest_2020-04-30_15-49-52.html', 'C:\\Users\\20126635\\PycharmProjects\\untitled\\Reports\\out.pdf')
# driver.quit()
# print ("test complete")
# time.sleep(2)
# HtmlTestRuuner=HtmlTestRunner
