#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import port
from router import app
import uvicorn


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=port, log_level="info")
    # gunicorn -b 127.0.0.1: 8001 -k uvicorn.workers.UvicornWorker wsgi:app
