from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    forgot_password_xpath = "//p[text()='Forgot your password? ']"
    user_name_field_name = "username"
    password_field_name = "password"
    login_button_xpath = "//button[text()=' Login ']"

    def click_forgot_password(self):
        self.element_click("forgot_password_xpath", self.forgot_password_xpath)

    def click_login_button(self, username, password):
        self.type_into_element(username, "user_name_field_name", self.user_name_field_name)
        self.type_into_element(password, "password_field_name", self.password_field_name)
        self.element_click("login_button_xpath", self.login_button_xpath)




