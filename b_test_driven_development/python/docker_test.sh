#!/bin/bash

 docker run \
    -v $(pwd):/data \
    -w /data \
    -t bkleinen/pytest \
    pytest -x tests/*.py
