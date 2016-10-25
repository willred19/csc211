#!/usr/bin/env python3

from flask import Flask, request, render_template
app = Flask(__name__)
app.config ['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return '<h1>"CSC211 HW7:Flask Assignment"</h1>
            <a href="localhost:5000">links page</a>'
