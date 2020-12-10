import os

from selenium.webdriver.remote.webdriver import WebDriver


DEFAULT_BROWSER = 'chrome'
AVAILABLE_BROWSERS = ['chrome', 'firefox']
BROWSER_HOSTS = {
    'chrome': 'chrome_provider',
    'firefox': 'firefox_provider'
}


class Browser(object):
    def __init__(self):
        browser_name = os.getenv('BROWSER', DEFAULT_BROWSER).lower()
        if browser_name not in AVAILABLE_BROWSERS:
            raise NotImplementedError('Browser "{0}" not available. Available browsers: {1}'.format(
                browser_name, AVAILABLE_BROWSERS))

        driver_host = BROWSER_HOSTS[browser_name]
        self.driver = WebDriver(
            command_executor='http://{0}:4444/wd/hub'.format(driver_host),
            desired_capabilities={"browserName": browser_name})

        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def close(self):
        self.driver.close()

    def go_to(self, url):
        self.driver.get(url)
        return self.driver
