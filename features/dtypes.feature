Feature: dtype support

  as a tester
  I want to be able to create column for all dtypes supported by pandas

  Scenario: All valid data
    Given a gherkin table as input
      | int         | int32         | int64         | float     | float32     | float64     | datetime     | datetime64     | object     | str                 |
      | integer_col | integer32_col | integer64_col | float_col | float32_col | float64_col | datetime_col | datetime64_col | object_col | str_col             |
      | 0           | 0             | 0             | 3.0       | 3.0         | 3.0         | 2018-02-01   | 2018-02-01     | egg        | silly walks         |
      | 1           | 10            | 100           | 4.1       | 4.1         | 4.1         | 2018-02-02   | 2018-02-02     | spam       | spanish inquisition |
      | 2           | 20            | 200           | 5.2       | 5.2         | 5.2         | 2018-02-03   | 2018-02-03     | bacon      | dead parrot         |
    When converted to a data frame using 1 row as column names and 0 column as index
    Then it matches a manually created data frame with correct dtypes