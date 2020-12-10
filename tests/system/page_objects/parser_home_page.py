from time import sleep
from selenium.webdriver.common.by import By

from tests.system.page_objects.base_page import BasePage, TRANSLATE_TO_UPPER
from tests.system.page_objects.about_us import AboutUsPage
from tests.system.page_objects.community_page import CommunityPage


class ParserHomePage(BasePage):
    section_xpath = "//nav[@class='nav']/ul/li[contains(" + TRANSLATE_TO_UPPER + ", '{section_name}')]"

    def go_to_section(self, section):
        section_pages = {
            'ABOUT US': AboutUsPage,
            'COMMUNITY': CommunityPage
        }
        if section.upper() not in section_pages:
            raise NotImplementedError('Automation for section "{0}" is not already implemented'.format(section))

        self.click_on(locator=(By.XPATH, self.section_xpath.format(section_name=section.upper())))
        sleep(3)
        return section_pages[section.upper()](self.driver)
