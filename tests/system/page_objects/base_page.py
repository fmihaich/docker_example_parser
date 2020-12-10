from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

TRANSLATE_TO_UPPER = "translate(., 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')"


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_textbox(self, locator, text_input):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        textbox = self.driver.find_element(*locator)
        textbox.click()
        textbox.clear()
        textbox.send_keys(text_input)

    def click_on(self, locator, web_element=None):
        driver = web_element if web_element else self.driver
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator))
        btn = driver.find_element(*locator)
        btn.click()

    def select_list_option(self, locator, option):
        by, value = locator[0], locator[1] + '[contains({0}, "{1}")]'.format(TRANSLATE_TO_UPPER, option.upper())
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((by, value)))
        list_option = self.driver.find_element(by, value)
        list_option.click()

    def get_web_element(self, locator, web_element=None):
        driver = web_element if web_element else self.driver
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locator))
        return driver.find_element(*locator)

    def get_web_elements(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located(locator))
        return self.driver.find_elements(*locator)

    def get_element_text(self, locator, web_element=None):
        driver = web_element if web_element else self.driver
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locator))
        element = driver.find_element(*locator)
        return element.text.strip()

    def get_element_texts(self, locator):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return [e.text.strip() if e.is_displayed() else '' for e in elements]

    def get_selector_selected_value(self, locator, web_element=None):
        selector = Select(self.get_web_element(locator, web_element))
        return selector.first_selected_option.text

    def is_any_element_displayed(self, locator):
        elements = self.driver.find_elements(*locator)
        return any([e.is_displayed() for e in elements])

    def is_checkbox_checked(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        checked = self.driver.execute_script(("return document.getElementById('%s').checked") % locator[1])
        return checked

    def wait_until_loaded(self, locator, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator))

    def wait_until_title_contains(self, title, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.title_contains(title))

    def wait_until_url_contains(self, url, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.url_contains(url))
