#!/bin/bash

 docker run \
    -v $(pwd):/data \
    -w /data \
    -t bkleinen/pytestjava \
    pytest -x -rx tests/*.py
