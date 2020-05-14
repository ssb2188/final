# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/clips")
def clippage():
    return render_template("clips.html")

@app.route("/memory")
def memorypage():
    return render_template("memory.html")

#start the server
if __name__ == "__main__":
    app.run()