#!/usr/bin/env bash
set -x

rm -rf dist build
python setup.py bdist_wheel