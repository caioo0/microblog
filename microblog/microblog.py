#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 10:53:24 2019
step 1:venv\Scripts\activate
step 2：flask run

@author: caichengxuan
"""

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
