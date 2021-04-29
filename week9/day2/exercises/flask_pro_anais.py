from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import pandas as pd
from os.path import join, dirname, realpath

app = Flask(__name__)
path = os.path.dirname( __file__ )

app.config["DEBUG"] = True

UPLOAD_FOLDER = ''
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route("/", methods=['POST'])
def uploadFiles():
    profile = request.files['file']
    profile.save(os.path.join(path + os.sep + "uploaded", secure_filename(profile.filename)))
    files = os.listdir(path + os.sep +"uploaded")

    for fil in files:
        if fil[-3:] == "csv":
            df = pd.read_csv(path + os.sep +"uploaded" + os.sep + fil)
            return "The file: " + fil + " has: " + str(df.shape[0]) + " rows"

        elif fil[-4:] == "json":
            df = pd.read_json(path + os.sep +"uploaded" + os.sep + fil)
            return "The file: " + fil + " has: " + str(df.shape[0]) + " rows"
        else:
            return "file not supported" 

if (__name__ == "__main__"):
     app.run(port = 5000)