#!/usr/bin/env python
# -*- coding: utf-8 -*-
from router import app
import uvicorn
import os

if __name__ == '__main__':
    uvicorn.run(app=app, host=os.getenv('HOST'), port=os.getenv('PORT'), log_level="info")
