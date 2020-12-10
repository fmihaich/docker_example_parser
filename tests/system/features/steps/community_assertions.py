import logging

from behave import step
from hamcrest import assert_that, is_in


@step('I see the following articles')
def assert_thought_articles_are_correctly_shown(context):
    community_thought_page = context.current_page
    articles = community_thought_page.get_thoughts_articles()
    logging.info('Shown articles in Community Thought section: {}'.format(articles))

    for row in context.table:
        assert_that(row['article'], is_in(articles))
