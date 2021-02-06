#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import port
from router import app, templates
import uvicorn

if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=port, log_level="info")
    # uvicorn manage:app --host 127.0.0.1 --port 8001
    # gunicorn manage:app -w 4 -k uvicorn.workers.UvicornWorker
