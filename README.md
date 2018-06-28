[![Build Status](https://travis-ci.com/Ge0f3/SpamDetection.svg?branch=master)](https://travis-ci.com/Ge0f3/SpamDetection) [![codecov](https://codecov.io/gh/Ge0f3/SpamDetection/branch/master/graph/badge.svg)](https://codecov.io/gh/Ge0f3/SpamDetection) ![pylint Score](https://mperlet.github.io/pybadge/badges/8.44.svg) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/e7d76d34801b493e83e97d98347c7362)](https://www.codacy.com/app/Ge0f3/SpamDetection?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Ge0f3/SpamDetection&amp;utm_campaign=Badge_Grade) [![HitCount](http://hits.dwyl.io/Ge0f3/Ge0f3/SpamDetection.svg)](http://hits.dwyl.io/Ge0f3/Ge0f3/SpamDetection)
# Data Science Web Application SpamDetection 

This is a Repository which Contains the implementation of ML model for spam detection 
# Live Demo 
The implementation of the web app can be found https://spamdetect.herokuapp.com/ <-- **here !**
# Deploy the app 
First fork or clone this repo:

usign `git clone https://github.com/Ge0f3/SpamDetection.git`

After cloning the repository go inside the project folder:

`cd SpamDetection`

Build docker using  `docker build -t spamapp:latest .` After deploy the app using `docker run -d -p 5000:5000 spamapp`

In your browser navigate to: `http://localhost:5000`(or whatever port you have mention in the docker build) to see the app up and running 

# Working without docker
I highly recommend the use of docker as it is far simpler to get started than to run all of the following manually.

**To Deploy manually**
Assure you have [Python](https://github.com/python). installed.
- Navigate inside the directory
- Install `pip dependencies: pip install -r requirements.txt`
- Run python `main.py` to see the app up and running (will watch files and restart server on port 5000 on change)
# Built With
- [Scikit](http://scikit-learn.org/stable/index.html) - scikit-learn is a Python module for machine learning
- [Flask](http://flask.pocoo.org/) - Flask is a microframework for Python
- [Docker](https://www.docker.com/) - Docker is an open platform and is used for building the app and Devops purposes
