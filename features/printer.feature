Feature: Table printer

  as a tester
  I want to be able to create gherkin tables from existing data frames

  Scenario: simple index and valid data
    Given a gherkin table as input
      | str       | float     | str                 | dict      | list     | OrderedDict              | OrderedDict      |
      | index_col | float_col | str_col             | dict_col  | list_col | ordered_dict_col         | ordered_dict_col |
      | egg       | 3.0       | silly walks         | {}        | []       | OrderedDict()            | []               |
      | spam      | 4.1       | spanish inquisition | {"a": 1}  | ["a"]    | OrderedDict([("a", 1)])  | [("a", 1)]       |
      | bacon     | 5.2       | dead parrot         | {"a": []} | [1]      | OrderedDict([("a", [])]) | [("a", [])]      |
    When converted to a data frame using 1 row as column names and 1 column as index
    And printed using data_frame_to_table
    Then it prints a valid string copy pasteable into gherkin files
    """
    | object    | float64   | object              | object    | object   | object                   | object                   |
    | index_col | float_col | str_col             | dict_col  | list_col | ordered_dict_col         | ordered_dict_col         |
    | egg       | 3.0       | silly walks         | {}        | []       | OrderedDict()            | OrderedDict()            |
    | spam      | 4.1       | spanish inquisition | {'a': 1}  | ['a']    | OrderedDict([('a', 1)])  | OrderedDict([('a', 1)])  |
    | bacon     | 5.2       | dead parrot         | {'a': []} | [1]      | OrderedDict([('a', [])]) | OrderedDict([('a', [])]) |
    """

  Scenario: handle None, nan, NaT
    Given a gherkin table as input
      | str       | float     | str         | datetime64[ns] | dict      | list     | OrderedDict              | OrderedDict      |
      | index_col | float_col | str_col     | datetime_col   | dict_col  | list_col | ordered_dict_col         | ordered_dict_col |
      | egg       |           | silly walks | 2018-02-02     |           | []       | OrderedDict([])          | []               |
      | spam      | 4.1       |             | 2018-02-03     | {"a": 1}  |          |                          |                  |
      | bacon     | 5.2       | dead parrot |                | {"a": []} | [1]      | OrderedDict([("a", [])]) | [("a", [])]      |
    When converted to a data frame using 1 row as column names and 1 column as index
    And printed using data_frame_to_table
    Then it prints a valid string copy pasteable into gherkin files
    """
    | object    | float64   | object      | datetime64[ns] | object    | object   | object                   | object                   |
    | index_col | float_col | str_col     | datetime_col   | dict_col  | list_col | ordered_dict_col         | ordered_dict_col         |
    | egg       |           | silly walks | 2018-02-02     |           | []       | OrderedDict()            | OrderedDict()            |
    | spam      | 4.1       |             | 2018-02-03     | {'a': 1}  |          |                          |                          |
    | bacon     | 5.2       | dead parrot |                | {'a': []} | [1]      | OrderedDict([('a', [])]) | OrderedDict([('a', [])]) |
    """