from pages.BasePage import BasePage


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators in ResetPasswordPage
    reset_user_name_filed_name = "username"
    reset_password_button_xpath = "//button[normalize-space()='Reset Password']"

    def sendkeys_user_name_and_click_reset_button(self):  # Check username field is enabled, enter username and click reset
        self.check_element_is_enabled("reset_user_name_filed_name", self.reset_user_name_filed_name)
        self.type_into_element("Nabe", "reset_user_name_filed_name", self.reset_user_name_filed_name)
        self.element_click("reset_password_button_xpath", self.reset_password_button_xpath)










