import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'static/scripts/detect_sentiment.py')
from detect_sentiment import detect_sentiment

from flask import Flask, render_template, jsonify
from flask_cors import CORS


###################################################
# Flask Setup
###################################################
app = Flask(__name__)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


###################################################
# Flask Routes
###################################################

#home page - index.html
@app.route("/")
def index():
    """List all available api routes."""
    return render_template("index.html")



#app page - input


if __name__ == '__main__':
    app.run(debug=True)
