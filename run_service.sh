#!/bin/sh

DIR_CONF="`dirname $0`/conf"

export PYTHONPATH="${PYTHONPATH}:DIR_CONF"

python deship/run.py