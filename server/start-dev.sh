#!/bin/bash

pip install -e /usr/src/app/packages/sxadapter/
pip install -e /usr/src/app/packages/sxmodel/

rainbow-saddle \
  --pid /tmp/app.pid gunicorn \
  -c /usr/src/app/gunicorn/gunicorn-dev.py \
  --chdir /usr/src/app main:app