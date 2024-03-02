import pytest
from pages.LoginPage import LoginPage
from pages.ResetPasswordPage import ResetPasswordPage

# TC_LOGIN_01 : Forgot password link validation on Login page


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_forgot_link_password_validation(self):

        login_page = LoginPage(self.driver)
        login_page.click_forgot_password()

        reset_password_page = ResetPasswordPage(self.driver)
        reset_password_page.sendkeys_user_name_and_click_reset_button()

        exp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
        assert self.driver.current_url == exp_url

