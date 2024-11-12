@skip.before.pandasv1
Feature: dtype support for new nullable dtypes in pandas 1.0

  as a tester
  I want to be able to create column for all the new nullable dtypes supported by pandas v1.0 and above

  Scenario: boolean dtype
    Given a gherkin table as input
      | boolean |
      | True    |
      | False   |
      |         |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid nullable boolean dtypes

  Scenario: integer dtype
    Given a gherkin table as input
      | Int64 |
      | 0     |
      | 10    |
      |       |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid nullable integer dtypes

  Scenario: string dtypes
    Given a gherkin table as input
      | string | string      |
      | egg    | silly walks |
      | spam   | ""          |
      |        | dead parrot |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid string dtypes

  Scenario: interval dtype
    Given a gherkin table as input
      | interval |
      | (0, 1]   |
      | (1, 2]   |
      |          |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid nullable interval dtypes

  Scenario: period dtype
    Given a gherkin table as input
      | period |
      | 2021Q1 |
      | 2021Q2 |
      |        |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid nullable period dtypes

  Scenario: categorical dtype
    Given a gherkin table as input
      | category |
      | A        |
      | B        |
      |          |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid nullable categorical dtypes
