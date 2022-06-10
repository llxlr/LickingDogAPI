#!/usr/bin/env python
# -*- coding: utf-8 -*-
from router import app
import uvicorn
import config

if __name__ == '__main__':
    uvicorn.run(app=app, host=config.HOST, port=config.PORT, log_level="info")
    #https://www.selenium.dev/selenium/docs/api/py/api.html
