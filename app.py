# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 11:36:10 2021

@author: zionh
"""

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'


    