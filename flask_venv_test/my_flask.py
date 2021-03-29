# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def my_view_func():
    return "This is an example page"