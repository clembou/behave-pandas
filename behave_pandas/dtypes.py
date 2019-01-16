import numpy as np

VALID_BOOL_DTYPES = {"bool": np.bool}

VALID_INT_DTYPES = {"int": np.int, "int32": np.int32, "int64": np.int64}

VALID_FLOAT_DTYPES = {"float": np.float, "float32": np.float32, "float64": np.float64}

VALID_DATETIME_DTYPES = {
    "datetime": np.datetime64,
    "datetime64": np.datetime64,
    "datetime64[ns]": np.datetime64,
}

VALID_OBJECT_DTYPES = {
    "object": object,
    "str": object,
    "dict": object,
    "list": object,
    "OrderedDict": object,
}

VALID_DTYPES = {
    **VALID_BOOL_DTYPES,
    **VALID_INT_DTYPES,
    **VALID_FLOAT_DTYPES,
    **VALID_DATETIME_DTYPES,
    **VALID_OBJECT_DTYPES,
}
