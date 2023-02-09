Feature: dtype support

  as a tester
  I want to be able to create column for all dtypes supported by pandas

  Scenario Outline: negative column or index level numbers
    Given a gherkin table as input
      | object | str         |
      | egg    | silly walks |

    When attempting to convert to a data frame using invalid number of row (<index_levels>) or column (<column_levels>) index levels
    Then it raises a ValueError Exception

    Examples:
      | index_levels | column_levels |
      | -1           | 0             |
      | 0            | -1            |
      | 3            | 0             |
      | 0            | 3             |
      | one          | 0             |
      | 0            | three         |
