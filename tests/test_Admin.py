import pytest
from pages.AdminPage import AdminPage
from pages.LoginPage import LoginPage
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    WebDriverException,
    InvalidSelectorException
)


# TC_PIM_02 : Header validation on Admin page


@pytest.mark.usefixtures("setup_and_teardown")
class TestAdmin:

    def test_header_validation_on_admin_page(self):  # To test headers in Admin page

        try:
            # Go to LoginPage to access driver
            login_page = LoginPage(self.driver)
            # Enter username, password and click login button
            login_page.click_login_button("Admin", "admin123")

            # Go to AdminPage to access driver
            admin_page = AdminPage(self.driver)
            # Click Admin
            admin_page.click_admin()

            expected_title = "OrangeHRM"
            # condition - to check current title = expected title
            assert self.driver.title.__eq__(expected_title)

            # condition - to check all headers visible in admin page
            assert admin_page.validate_displaying_options_on_admin_page()

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, WebDriverException,
                InvalidSelectorException) as e:
            print(f"Exception occurred: {type(e).__name__}: {e}")
            return None  # any default value suitable for your case

# TC_PIM_03 : Main menu validation on Admin page

    def test_options_menu_validation_on_admin_page(self):   # To test Main menu options in Admin page

        try:
            # Go to LoginPage to access driver
            login_page = LoginPage(self.driver)
            # Enter username, password and click login button
            login_page.click_login_button("Admin", "admin123")

            # Go to AdminPage to access driver
            admin_page = AdminPage(self.driver)
            # Click Admin
            admin_page.click_admin()

            # condition - to check all main menu visible in admin page
            assert admin_page.validate_menu_displaying_on_admin_page()

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, WebDriverException,
                InvalidSelectorException) as e:
            print(f"Exception occurred: {type(e).__name__}: {e}")
            return None  # any default value suitable for your case
