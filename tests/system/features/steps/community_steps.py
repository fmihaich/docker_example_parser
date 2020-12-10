from behave import step


@step('I go to "{blog_name}" blog')
def navigate_to_section(context, blog_name):
    community_page = context.current_page
    community_page.go_to_blog(blog_name)
