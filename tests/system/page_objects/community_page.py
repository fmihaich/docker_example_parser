from time import sleep
from selenium.webdriver.common.by import By

from tests.system.page_objects.base_page import BasePage, TRANSLATE_TO_UPPER


class CommunityPage(BasePage):
    blog_xpath = "//ul[@id='menu-blog-menu']/li[contains(" + TRANSLATE_TO_UPPER + ", '{section_name}')]"
    thoughts_article_locator = (By.XPATH, "//div[@class='blog-item-content']/h2/a")

    def go_to_blog(self, blog_name):
        self.click_on(locator=(By.XPATH, self.blog_xpath.format(section_name=blog_name.upper())))
        sleep(1)

    def get_thoughts_articles(self):
        return self.get_element_texts(locator=self.thoughts_article_locator)
