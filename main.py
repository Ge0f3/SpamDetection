import numpy as np 
from flask import jsonify,abort,request,Flask
from flask import Flask, render_template, request
import pickle,joblib
import json


my_predict = pickle.load(open('model_file','rb'))
ser_countvect =pickle.load(open('countvect','rb'))

#using joblib
# my_predict = joblib.load('model.pkl')
# ser_countvect=joblib.load('countvect.pkl')

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api', methods=['POST'])
def get_delay():
    result=request.form

    productname = result['email']
    # we create a json object that will hold data from user inputs
    product = [productname]
    x_count = ser_countvect.transform(product)
    # encode the json object to one hot encoding so that it could fit our model
    # get the price prediction
    res = my_predict.predict(x_count)
    #output = res[0]
    # return a json value
    app.logger.info("The type of the producname is {}".format(res))
    return json.dumps({'result':res[0]});

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)