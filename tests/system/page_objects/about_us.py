from selenium.webdriver.common.by import By

from tests.system.page_objects.base_page import BasePage


class AboutUsPage(BasePage):
    team_member_locator = (By.XPATH, "//div[@id='team']/div/div/div/a/h4")

    def get_team_members(self):
        return self.get_element_texts(locator=self.team_member_locator)
