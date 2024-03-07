from flask import Flask
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "Hello there!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)