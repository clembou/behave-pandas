Feature: dtype support

  as a tester
  I want to be able to create columns with missing data where supported by pandas

  Scenario: bool dtypes
    Given a gherkin table as input
      | bool  | bool |
      | True  |      |
      |       |      |
      | true  |      |
      | false |      |
    When attempting to convert to a data frame using 0 row as column names and 0 column as index
    Then it raises a ValueError exception

  Scenario: integer dtypes
    Given a gherkin table as input
      | int | int |
      |     |     |
      | 1   |     |
      | 2   |     |
    When attempting to convert to a data frame using 0 row as column names and 0 column as index
    Then it raises a ValueError exception

  Scenario: float dtypes
    Given a gherkin table as input
      | float | float |
      |       |       |
      | 4.1   |       |
      | 5.2   |       |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with null float data

  Scenario: datetime dtypes
    Given a gherkin table as input
      | datetime   | datetime |
      | 2018-02-01 |          |
      |            |          |
      | 2018-02-03 |          |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with null datetime data

  Scenario: object dtypes
    Given a gherkin table as input
      | object | str | dict | list |
      | egg    |     |      |      |
      |        |     |      |      |
      | bacon  |     |      |      |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with null object data

  Scenario: empty table
    Given a gherkin table as input
      | object | str | float | datetime | dict | list |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created empty data frame