import logging

from behave import step
from hamcrest import assert_that, is_in


@step('I see the management team is composed by')
def assert_team_members_are_correctly_shown(context):
    about_us_page = context.current_page
    team_members = about_us_page.get_team_members()
    logging.info('Shown team members: {}'.format(team_members))

    for row in context.table:
        assert_that(row['name'], is_in(team_members))
