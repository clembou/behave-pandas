Feature: multi index support

  as a tester
  I want to be able to create data frame with a specific index with a configurable number of levels

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

  Scenario: multi index on columns and single row index
    Given a gherkin table as input
      | str     | int | int | float  | float  |
      | country | age | age | height | height |
      |         | min | max | min    | max    |
      | France  | 3   | 9   | 15.0   | 18.0   |
      | UK      | 4   | 8   | 13.1   | 19.2   |
      | USA     | 5   | 10  | 12.2   | 15.7   |
    When converted to a data frame using 2 row as column names and 1 column as index
    Then it matches a manually created data frame with a multi index on columns and single row index

  Scenario: multi index on columns and multi row index
    Given a gherkin table as input
      | str     | str        | int | int | float  | float  |
      | country | city       | age | age | height | height |
      |         |            | min | max | min    | max    |
      | France  | Nantes     | 3   | 9   | 15.0   | 18.0   |
      | France  | Paris      | 5   | 11  | 16.0   | 21.0   |
      | UK      | London     | 4   | 8   | 13.1   | 19.2   |
      | UK      | Manchester | 2   | 6   | 8.1    | 11.2   |
    When converted to a data frame using 2 row as column names and 2 column as index
    Then it matches a manually created data frame with a multi index on columns and multi row index

  Scenario: multi index on columns and multi row index, index name flattening disabled
    Given a gherkin table as input
      | str     | str        | int | int | float  | float  |
      | country | city       | age | age | height | height |
      |         |            | min | max | min    | max    |
      | France  | Nantes     | 3   | 9   | 15.0   | 18.0   |
      | France  | Paris      | 5   | 11  | 16.0   | 21.0   |
      | UK      | London     | 4   | 8   | 13.1   | 19.2   |
      | UK      | Manchester | 2   | 6   | 8.1    | 11.2   |
    When converted to a data frame using 2 row as column names and 2 column as index without flattening index names
    Then it matches a manually created data frame with a multi index on columns and multi row index and unflattened index names

  Scenario: index level choice does not matter if the index name flattening is on
    Given a gherkin table as input
      | str     | str        | int | int | float  | float  |
      | country | city       | age | age | height | height |
      |         |            | min | max | min    | max    |
      | France  | Nantes     | 3   | 9   | 15.0   | 18.0   |
      | France  | Paris      | 5   | 11  | 16.0   | 21.0   |
      | UK      | London     | 4   | 8   | 13.1   | 19.2   |
      | UK      | Manchester | 2   | 6   | 8.1    | 11.2   |
    When converted to a data frame using 2 row as column names and 2 column as index
    Then it matches a similar table definition where index column names have been set on the second row
      | str     | str        | int | int | float  | float  |
      |         |            | age | age | height | height |
      | country | city       | min | max | min    | max    |
      | France  | Nantes     | 3   | 9   | 15.0   | 18.0   |
      | France  | Paris      | 5   | 11  | 16.0   | 21.0   |
      | UK      | London     | 4   | 8   | 13.1   | 19.2   |
      | UK      | Manchester | 2   | 6   | 8.1    | 11.2   |

  Scenario: multi index on columns and multi row index, index name flattening disabled, complex column name combination
    Given a gherkin table as input
      | str     | str        | int | int | float  | float  |
      | country | city       | age | age | height | height |
      |         |            |     | max | min    | max    |
      | France  | Nantes     | 3   | 9   | 15.0   | 18.0   |
      | France  | Paris      | 5   | 11  | 16.0   | 21.0   |
      | UK      | London     | 4   | 8   | 13.1   | 19.2   |
      | UK      | Manchester | 2   | 6   | 8.1    | 11.2   |
    When converted to a data frame using 2 row as column names and 3 column as index without flattening index names
    Then it matches a manually created data frame with a multi index on columns and multi row index and complex column name combination