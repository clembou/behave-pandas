Feature: Table printer

  as a tester
  I want to be able to create gherkin tables from existing data frames

  Scenario: simple index and valid data
    Given a gherkin table as input
      | str       | float     | str                 |
      | index_col | float_col | str_col             |
      | egg       | 3.0       | silly walks         |
      | spam      | 4.1       | spanish inquisition |
      | bacon     | 5.2       | dead parrot         |
    When converted to a data frame using 1 row as column names and 1 column as index
    And printed using data_frame_to_table
    Then it prints a valid string copy pasteable into gherkin files
    """
    | object    | float64   | object              |
    | index_col | float_col | str_col             |
    | egg       | 3.0       | silly walks         |
    | spam      | 4.1       | spanish inquisition |
    | bacon     | 5.2       | dead parrot         |
    """

  Scenario: handle None, nan, NaT
    Given a gherkin table as input
      | str       | float     | str         | datetime64[ns] |
      | index_col | float_col | str_col     | datetime_col   |
      | egg       |           | silly walks | 2018-02-02     |
      | spam      | 4.1       |             | 2018-02-03     |
      | bacon     | 5.2       | dead parrot |                |
    When converted to a data frame using 1 row as column names and 1 column as index
    And printed using data_frame_to_table
    Then it prints a valid string copy pasteable into gherkin files
    """
    | object    | float64   | object      | datetime64[ns] |
    | index_col | float_col | str_col     | datetime_col   |
    | egg       |           | silly walks | 2018-02-02     |
    | spam      | 4.1       |             | 2018-02-03     |
    | bacon     | 5.2       | dead parrot |                |
    """