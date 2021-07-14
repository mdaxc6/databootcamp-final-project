import numpy as np
import pandas as pd
from flask import Flask, render_template, jsonify


###################################################
# Flask Setup
###################################################
app = Flask(__name__)


###################################################
# Flask Routes
###################################################

#home page - index.html
@app.route("/")
def index():
    """List all available api routes."""
    return render_template("index.html")



#app page - input

