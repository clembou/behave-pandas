Feature: multi index support

  as a tester
  I want to be able to create data frame with a specific index

  Scenario: simple index
    Given a gherkin table as input
      | str       | float     | str                 |
      | index_col | float_col | str_col             |
      | egg       | 3.0       | silly walks         |
      | spam      | 4.1       | spanish inquisition |
      | bacon     | 5.2       | dead parrot         |
    When converted to a data frame using 1 row as column names and 1 column as index
    Then it matches a manually created data frame with a single index

  Scenario: multi index
    Given a gherkin table as input
      | str       | float     | str                 |
      | index_col | float_col | str_col             |
      | egg       | 3.0       | silly walks         |
      | spam      | 4.1       | spanish inquisition |
      | bacon     | 5.2       | dead parrot         |
    When converted to a data frame using 1 row as column names and 2 column as index
    Then it matches a manually created data frame with a multi index

  Scenario: multi index on columns
    Given a gherkin table as input
      | str     | int | int | float  | float  |
      | country | age | age | height | height |
      |         | min | max | min    | max    |
      | France  | 3   | 9   | 15.0   | 18.0   |
      | UK      | 4   | 8   | 13.1   | 19.2   |
      | USA     | 5   | 10  | 12.2   | 15.7   |
    When converted to a data frame using 2 row as column names and 0 column as index
    Then it matches a manually created data frame with a multi index on columns