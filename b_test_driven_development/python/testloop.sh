#!/bin/bash

echo "-----1: ----$1"
if [ $1 ]; then
    subdir=$1
else
    subdir=tests
fi

# echo "-----subdir: ----$subdir"

while true; do
    clear
    # pytest -x -vv $subdir
    pytest -vv -x ${subdir}
    # pytest  tests/importer/moneymoneyimporter_amex_usd_test.py
    fswatch ./**/*.py  -1
done