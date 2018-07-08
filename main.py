#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pickle
import json
from flask import jsonify , request, Flask, render_template

myPredict = pickle.load(open('model_file', 'rb'))
ser_countvect = pickle.load(open('countvect', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/card')
def card():
    return render_template('card.html')

@app.route('/api', methods=['POST'])
def model():
    result = request.form
    productname = result['email']

    # we create a json object that will hold data from user inputs

    product = [productname]
    x_count = ser_countvect.transform(product)

    # encode the json object to one hot encoding so that it could fit our model
    # get the  prediction

    res = myPredict.predict(x_count)

    # return a json value

    #app.logger.info('The type of the producname is {}'.format(res))
    return json.dumps({'result': res[0]})


@app.route('/test', methods=['post'])
def predict():
    word = request.get_json(force=True)
    x_count = ser_countvect.transform(word)
    res = myPredict.predict(x_count)
    output = res[0]
    return jsonify(results=output)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
