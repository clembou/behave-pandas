Feature: dtype support

  as a tester
  I want to be able to create column for all dtypes supported by pandas

  Scenario: bool dtypes
    Given a gherkin table as input
      | bool  |
      | True  |
      | False |
      | true  |
      | false |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid boolean dtypes

  Scenario: integer dtypes
    Given a gherkin table as input
      | int | int32 | int64 |
      | 0   | 0     | 0     |
      | 1   | 10    | 100   |
      | 2   | 20    | 200   |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid integer dtypes

  Scenario: float dtypes
    Given a gherkin table as input
      | float | float32 | float64 |
      | 3.0   | 3.0     | 3.0     |
      | 4.1   | 4.1     | 4.1     |
      | 5.2   | 5.2     | 5.2     |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid float dtypes

  Scenario: datetime dtypes
    Given a gherkin table as input
      | datetime   | datetime64 | datetime64[ns] |
      | 2018-02-01 | 2018-02-01 | 2018-02-01     |
      | 2018-02-02 | 2018-02-02 | 2018-02-02     |
      | 2018-02-03 | 2018-02-03 | 2018-02-03     |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid datetime dtypes

  Scenario: object dtypes
    Given a gherkin table as input
      | object | str                 | dict        | list  | OrderedDict            | OrderedDict                         |
      | egg    | silly walks         | {}          | []    | []                     | OrderedDict([])                     |
      | spam   | spanish inquisition | {"a": None} | [1]   | [("a", 1),("b", None)] | OrderedDict([("a", 1),("b", None)]) |
      | bacon  | dead parrot         | {"a": []}   | ["a"] | [("a", 1),("b", [])]   | OrderedDict([("a", 1),("b", [])])   |
    When converted to a data frame using 0 row as column names and 0 column as index
    Then it matches a manually created data frame with all valid object dtypes

  Scenario: invalid dtypes
    Given a gherkin table as input
      | object | invalid             |
      | egg    | silly walks         |
      | spam   | spanish inquisition |
      | bacon  | dead parrot         |
    When attempting to convert to a data frame using 0 row as column names and 0 column as index
    Then it raises an Exception