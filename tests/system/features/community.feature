Feature: Parser Community

  Background:
    Given I navigate to "Parser Digital" home page

  @DEMO
  Scenario: Thought are shown in community section
    When I navigate to "Community" page
    And I go to "Thoughts" blog
    Then I see the following articles:
      | article                                           |
      | Automation testing vs Manual testing              |
      | How to Create an Effective QA Automation Strategy |
      | Demystifying Thread Safety                        |
