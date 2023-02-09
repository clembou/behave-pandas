#!/usr/bin/env bash
set -x

rm -rf dist build behave_pandas.egg-info
python -m build --wheel