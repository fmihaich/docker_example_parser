import logging
from behave import step

from tests.system.page_objects.parser_home_page import ParserHomePage

PARSER_HOME_PAGE = 'https://parserdigital.com/'


@step('I navigate to "Parser Digital" home page')
def navigate_to_rch_page(context):
    logging.info('Parser home page URL: "{0}"'.format(PARSER_HOME_PAGE))
    context.browser = context.browser.go_to(PARSER_HOME_PAGE)
    context.current_page = ParserHomePage(context.browser)


@step('I navigate to "{section}" page')
def navigate_to_section(context, section):
    home_page = context.current_page
    section_page = home_page.go_to_section(section)
    context.current_page = section_page


@step('I scroll down')
def scroll_down(context):
    context.current_page.scroll_down()
