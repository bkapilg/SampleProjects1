class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_testbox_id = "txtUsername"
        self.password_testbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.invalidusername_message_id = "spanMessage"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_testbox_id).clear()
        self.driver.find_element_by_id(self.username_testbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_testbox_id).clear()
        self.driver.find_element_by_id(self.password_testbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def check_invalid_username_message(self, message):
        msg = self.driver.find_element_by_id(self.invalidusername_message_id).text()
        return msg
