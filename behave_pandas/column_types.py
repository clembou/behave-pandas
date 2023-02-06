import ast
from collections import OrderedDict

import numpy as np
import pandas as pd


class ColumnParser:
    def __init__(self, pandas_dtype_name):
        self.pandas_dtype_name = pandas_dtype_name

    def parse_value(self, cell):
        pass


class DatetimeColumnParser(ColumnParser):
    def __init__(self):
        super().__init__("datetime64[ns]")

    def parse_value(self, cell):
        if cell == "":
            return np.nan
        else:
            return np.datetime64(cell)


class LegacyStringColumnParser(ColumnParser):
    def __init__(self):
        super().__init__("object")

    def parse_value(self, cell):
        if cell == "":
            return np.nan
        elif cell == '""':
            return ""
        else:
            return cell


class StringColumnParser(ColumnParser):
    def __init__(self):
        super().__init__("string")

    def parse_value(self, cell):
        if cell == "":
            return pd.NA
        elif cell == '""':
            return ""
        else:
            return cell


class FloatColumnParser(ColumnParser):
    VALID_FLOAT_DTYPES = {
        "float": float,
        "float32": np.float32,
        "float64": np.float64,
    }

    def parse_value(self, cell):
        if cell == "":
            return np.nan
        else:
            return self.VALID_FLOAT_DTYPES[self.pandas_dtype_name](cell)


class LegacyIntegerColumnParser(ColumnParser):
    VALID_PANDAS_DTYPES = {
        "int": int,
        "int32": np.int32,
        "int64": np.int64,
    }

    def parse_value(self, cell):
        if cell == "":
            return np.nan
        else:
            return self.VALID_PANDAS_DTYPES[self.pandas_dtype_name](cell)


class NullableIntegerColumnParser(ColumnParser):
    def __init__(self):
        super().__init__("Int64")

    def parse_value(self, cell):
        if cell == "":
            return pd.NA
        else:
            return np.int64(cell)


class LegacyBooleanColumnParser(ColumnParser):
    def __init__(self):
        super().__init__("bool")

    def parse_value(self, cell):
        if cell.lower() == "true":
            return True
        elif cell.lower() == "false":
            return False
        elif cell == "":
            raise ValueError("null values are not supported for bool columns.")
        else:
            raise ValueError("{} cannot be parsed as a bool".format(cell))


class NullableBooleanColumnParser(ColumnParser):
    def __init__(self):
        super().__init__("boolean")

    def parse_value(self, cell):
        if cell.lower() == "true":
            return True
        elif cell.lower() == "false":
            return False
        elif cell == "":
            return pd.NA
        else:
            raise ValueError("{} cannot be parsed as a boolean".format(cell))


class ListColumnParser(ColumnParser):
    def __init__(self):
        super().__init__("object")

    def parse_value(self, cell):
        if cell == "":
            return np.nan
        else:
            return ast.literal_eval(cell)


class DictColumnParser(ColumnParser):
    def __init__(self):
        super().__init__("object")

    def parse_value(self, cell):
        if cell == "":
            return np.nan
        else:
            return ast.literal_eval(cell)


class OrderedDictColumnParser(ColumnParser):
    def __init__(self):
        super().__init__("object")

    def parse_value(self, cell):
        if cell == "":
            return np.nan
        else:
            cell_cleaned = cell.replace("OrderedDict(", "").rstrip(")")
            if cell_cleaned == "":
                return OrderedDict()
            return OrderedDict(ast.literal_eval(cell_cleaned))


class ObjectColumnParser(ColumnParser):
    def __init__(self):
        super().__init__("object")

    def parse_value(self, cell):
        if cell == "":
            return np.nan
        else:
            return cell


VALID_BOOL_TYPES = {
    "bool": LegacyBooleanColumnParser(),
}

VALID_INT_TYPES = {
    "int": LegacyIntegerColumnParser("int"),
    "int32": LegacyIntegerColumnParser("int32"),
    "int64": LegacyIntegerColumnParser("int64"),
}

VALID_FLOAT_TYPES = {
    "float": FloatColumnParser("float"),
    "float32": FloatColumnParser("float32"),
    "float64": FloatColumnParser("float64"),
}

VALID_DATETIME_TYPES = {
    "datetime": DatetimeColumnParser(),
    "datetime64": DatetimeColumnParser(),
    "datetime64[ns]": DatetimeColumnParser(),
}

VALID_OBJECT_TYPES = {
    "object": ObjectColumnParser(),
    "str": LegacyStringColumnParser(),
    "dict": DictColumnParser(),
    "list": ListColumnParser(),
    "OrderedDict": OrderedDictColumnParser(),
}

# new nullable type from pandas 1.0
VALID_NULLABLE_TYPES = {
    "boolean": NullableBooleanColumnParser(),
    "Int64": NullableIntegerColumnParser(),
    "string": StringColumnParser(),
}

VALID_COLUMN_TYPES = {
    **VALID_BOOL_TYPES,
    **VALID_INT_TYPES,
    **VALID_FLOAT_TYPES,
    **VALID_DATETIME_TYPES,
    **VALID_NULLABLE_TYPES,
    **VALID_OBJECT_TYPES,
}
