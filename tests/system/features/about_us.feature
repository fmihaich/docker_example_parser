Feature: About us

  Background:
    Given I navigate to "Parser Digital" home page


  Scenario: Management team is shown in about us section
    When I navigate to "About us" page
    Then I see the management team is composed by:
      | name            |
      | Ricardo Moral   |
      | Hernan Griboff  |
      | Luciano Griboff |
      | Geoff Goodhew   |
      | Leonel Mazal    |
      | Tiago Miguel    |
      | Juana Furlong   |
      | Gabriela Puyo   |
