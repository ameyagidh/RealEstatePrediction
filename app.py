import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

## Load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))
@app.route('/')
def home():

    return render_template("home.html")

@app.route("/predict",methods=["POST"])
def predict():
    data = request.json["data"]
    print(data)
    return render_template("")
