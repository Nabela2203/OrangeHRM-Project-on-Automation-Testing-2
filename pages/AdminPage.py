from pages.BasePage import BasePage


class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators in AdminPage
    admin_menu_link_text = "Admin"
    user_management_xpath = "//span[text()='User Management ']"
    job_xpath = "//span[text()='Job ']"
    organization_xpath = "//span[text()='Organization ']"
    qualifications_xpath = "//span[text()='Qualifications ']"
    nationalities_link_text = "Nationalities"
    corporate_branding_link_text = "Corporate Branding"
    configuration_xpath = "//span[text()='Configuration ']"
    pim_menu_link_text = "PIM"
    leave_menu_link_text = "Leave"
    time_menu_link_text = "Time"
    recruitment_menu_link_text = "Recruitment"
    my_info_menu_link_text = "My Info"
    performance_menu_link_text = "Performance"
    dashboard_menu_link_text = "Dashboard"
    directory_menu_link_text = "Directory"
    maintenance_menu_link_text = "Maintenance"
    claim_menu_link_text = "Claim"
    buzz_menu_link_text = "Buzz"

    def click_admin(self):  # To click Admin menu
        self.element_click("admin_menu_link_text", self.admin_menu_link_text)

    def validate_displaying_options_on_admin_page(self):  # To validate header options are visible in AdminPage

        user_management = self.check_display_status_of_element("user_management_xpath", self.user_management_xpath)
        job = self.check_display_status_of_element("job_xpath", self.job_xpath)
        organization = self.check_display_status_of_element("organization_xpath", self.organization_xpath)
        qualifications = self.check_display_status_of_element("qualifications_xpath", self.qualifications_xpath)
        nationalities = self.check_display_status_of_element("nationalities_link_text", self.nationalities_link_text)
        corporate_branding = self.check_display_status_of_element("corporate_branding_link_text", self.corporate_branding_link_text)
        configuration = self.check_display_status_of_element("configuration_xpath", self.configuration_xpath)

        if user_management and job and organization and qualifications and nationalities and corporate_branding and configuration:
            return True
        else:
            return False

    def validate_menu_displaying_on_admin_page(self):  # To validate main menu options are visible in AdminPage

        pim = self.check_display_status_of_element("pim_menu_link_text", self.pim_menu_link_text)
        leave = self.check_display_status_of_element("leave_menu_link_text", self.leave_menu_link_text)
        time = self.check_display_status_of_element("time_menu_link_text", self.time_menu_link_text)
        recruitment = self.check_display_status_of_element("recruitment_menu_link_text", self.recruitment_menu_link_text)
        my_info = self.check_display_status_of_element("my_info_menu_link_text", self.my_info_menu_link_text)
        performance = self.check_display_status_of_element("performance_menu_link_text", self.performance_menu_link_text)
        dashboard = self.check_display_status_of_element("dashboard_menu_link_text", self.dashboard_menu_link_text)
        directory = self.check_display_status_of_element("directory_menu_link_text", self.directory_menu_link_text)
        maintenance = self.check_display_status_of_element("maintenance_menu_link_text", self.maintenance_menu_link_text)
        claim = self.check_display_status_of_element("claim_menu_link_text", self.claim_menu_link_text)
        buzz = self.check_display_status_of_element("buzz_menu_link_text", self.buzz_menu_link_text)

        if pim and leave and time and recruitment and my_info and performance and dashboard and directory and maintenance and claim and buzz:
            return True
        else:
            return False