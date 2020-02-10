# behave-pandas

Utility package for the [Behave](https://github.com/behave/behave) BDD testing framework, to make converting gherkin tables
to and from [pandas](https://github.com/pandas-dev/pandas) data frames a breeze.

## Build Status
![Travis CI badge](https://travis-ci.org/clembou/behave-pandas.svg?branch=master)

## Installation

```bash
pip install behave-pandas
```

## Features

* Easily convert a Gherkin table into a pandas data frame with explicit dtype information
* Easily convert a pandas data frame into a behave table that can be parsed by behave-pandas
* Support converting data frames with multiple index levels either on columns or rows
* Handle missing data for dtypes that support it.

## Changelog

[See the changelog here.](CHANGELOG.md)

## API

The behave-pandas api is extremely simple, and consists in two functions:

```python
from behave_pandas import table_to_dataframe, dataframe_to_table
```

## Example

```gherkin
Feature: Table printer

  as a tester
  I want to be able to create gherkin tables from existing data frames

  Scenario: simple index
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
```

Associated steps:

```python
from behave import *
from behave_pandas import table_to_dataframe, dataframe_to_table

use_step_matcher("parse")

@given("a gherkin table as input")
def step_impl(context,):
    context.input = context.table

@when('converted to a data frame using {column_levels:d} row as column names and {index_levels:d} column as index')
def step_impl(context, column_levels, index_levels):
    context.parsed = table_to_dataframe(context.input, column_levels=column_levels, index_levels=index_levels)


@then("it prints a valid string copy pasteable into gherkin files")
def step_impl(context):
    assert context.result == context.text


@step("printed using data_frame_to_table")
def step_impl(context):
    context.result = dataframe_to_table(context.parsed)
```

Parsed dataframe:

```
>>> context.parsed
           float_col              str_col
index_col
egg              3.0          silly walks
spam             4.1  spanish inquisition
bacon            5.2          dead parrot

>>> context.parsed.info()
<class 'pandas.core.frame.DataFrame'>
Index: 3 entries, egg to bacon
Data columns (total 2 columns):
float_col    3 non-null float64
str_col      3 non-null object
dtypes: float64(1), object(1)
memory usage: 72.0+ bytes
```
