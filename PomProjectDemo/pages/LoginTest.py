import HtmlTestRunner
from selenium import webdriver
import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))

from POMProject.Pages.loginPage import LoginPage
from POMProject.Pages.Homepage import HomePage



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/rcwboat/Desktop/drivers/chromedriver")
        cls.driver.maximize_window()


    def test_login_valid(self):
        driver = self.driver
        driver.get("https://freecrm.com/")
        login = LoginPage(driver)
        login.click_logininhome()
        login.enter_username("sairamboopathi@gmail.com")
        login.enter_password("Sairam@123")
        login.click_loginbutton()

        homepage = HomePage(driver)
        homepage.click_Contact()
        homepage.clickHomelogoutButton()
        homepage.clickLogout()

        if __name__ == '__main__':
         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output='/Users/rcwboat/PycharmProjects/SeleniumPrgms/POMProject/reports'))

