#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import port
from router import app
import argparse
import uvicorn

parser = argparse.ArgumentParser(description='Config Options')
parser.add_argument('-E', '--env', help='custom PATH of dotenv file')
args = parser.parse_args()

if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=port, log_level="info")
