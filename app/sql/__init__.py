#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sql import models
from sql.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
