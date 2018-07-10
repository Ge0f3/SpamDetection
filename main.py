#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pickle
import json
import pandas as pd
import numpy as np 
from flask import jsonify , request, Flask, render_template,redirect,url_for,send_file
from werkzeug.utils import secure_filename
from werkzeug import SharedDataMiddleware

myPredict = pickle.load(open('model_file', 'rb'))
ser_countvect = pickle.load(open('countvect', 'rb'))

UPLOAD_FOLDER = '/Users/geofe/Documents/workspace/Projects/Spam_filtering/webapp/uploads'
ALLOWED_EXTENSIONS = set(['csv', 'pdf', 'json', 'txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})




@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/test-file')
def download():
    try:
        return send_file('./Model/spam.csv',attachment_filename='spam.csv')
    except Exception as e:
        return str(e)

@app.route('/chart')
def chart():
    legend = 'Monthly Data'
    labels = ["Bogus", "Real"]
    values = [20, 80]
    return render_template('chart.html', values=values, labels=labels, legend=legend)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            df = pd.read_csv(file,encoding='latin-1')
            print(df.head())
            try:
                x_trans=ser_countvect.transform(df.v2)
                predicted_values = myPredict.predict(x_trans)
                value,counts = np.unique(predicted_values,return_counts=True)
                legend ='HAM VS SPAM'
                labels=[value[0],value[1]]
                values=[counts[0],counts[1]]
                print("The labels are {}\nThe counts are {}".format(labels,values))
                return render_template('chart.html', values=values, labels=labels, legend=legend)
            except AttributeError as error:
                #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('index'))
            else:
                return redirect(url_for('index'))
            # return redirect(url_for('home'))
    #return render_template('chart.html', values=values, labels=labels, legend=legend)
    # return redirect(url_for('index'))
    return render(url_for('chart', values=values, labels=labels, legend=legend))



if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
