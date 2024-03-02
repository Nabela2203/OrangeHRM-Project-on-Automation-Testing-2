import pytest
from pages.AdminPage import AdminPage
from pages.LoginPage import LoginPage

# TC_PIM_02 : Header validation on Admin page


@pytest.mark.usefixtures("setup_and_teardown")
class TestAdmin:

    def test_header_validation_on_admin_page(self):

        login_page = LoginPage(self.driver)
        login_page.click_login_button("Admin", "admin123")

        admin_page = AdminPage(self.driver)
        admin_page.click_admin()

        expected_title = "OrangeHRM"
        assert self.driver.title.__eq__(expected_title)

        assert admin_page.validate_displaying_options_on_admin_page()

# TC_PIM_03 : Main menu validation on Admin page

    def test_options_menu_validation_on_admin_page(self):

        login_page = LoginPage(self.driver)
        login_page.click_login_button("Admin", "admin123")

        admin_page = AdminPage(self.driver)
        admin_page.click_admin()

        assert admin_page.validate_menu_displaying_on_admin_page()

