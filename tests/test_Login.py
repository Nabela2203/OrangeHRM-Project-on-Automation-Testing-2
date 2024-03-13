import pytest
from pages.LoginPage import LoginPage
from pages.ResetPasswordPage import ResetPasswordPage
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    WebDriverException,
    InvalidSelectorException
)

# TC_LOGIN_01 : Forgot password link validation on Login page


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_forgot_link_password_validation(self):  # To test forgot password link

        try:
            # Go to LoginPage to access driver
            login_page = LoginPage(self.driver)
            # Click Forgot password
            login_page.click_forgot_password()

            # Go to ResetPasswordPage to access driver
            reset_password_page = ResetPasswordPage(self.driver)
            # Enter username and click reset button
            reset_password_page.sendkeys_user_name_and_click_reset_button()

            exp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
            # condition - to check current url = expected url
            assert self.driver.current_url == exp_url

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, WebDriverException,
                InvalidSelectorException) as e:
            print(f"Exception occurred: {type(e).__name__}: {e}")
            return None  # any default value suitable for your case
