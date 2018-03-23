from flask import render_template, abort, request
from flask_login import login_required, current_user
from sklearn import linear_model
import pickle

from . import home


# Output is the probability that the given input (ex. email) belongs to a certain class (ex. spam or not)
logReg = linear_model.LogisticRegression()
# Samples (your features, they should be normalized  and standardized). Normalization scales the values
# into a range of [0,1]. Standardization scales data to have a mean of 0 and standard deviation of 1
# Note that we are using fake data here just to demonstrate the concept
X = [[1.0, 1.0, 2.1], [2.0, 2.2, 3.3], [3.0, 1.1, 3.0]]
# Labeled data (Spam or not)
Y = [1, 0, 1]
# Build the model
logReg.fit(X, Y)
pickle.dump(logReg, open('logReg.pkl', 'wb'))


@home.route('/')
def homepage():
    """
    Render the home apge template
    """
    return render_template('home/index.html', title='welcome')


@home.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html', title='Dashboard')


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title='Admin dashboard')


@home.route('/data-sources')
@login_required
def data_sources():
    return render_template('home/data-sources.html', title='Data Sources')


@home.route('/regression', methods=['GET'])
@login_required
def display_regression():
    """
    We estimate the probabilities here
    """
    # We are using 3 features. For example: subject line, word frequency, etc
    param1 = float(request.args.get('p1'))
    param2 = float(request.args.get('p2'))
    param3 = float(request.args.get('p3'))
    logReg = pickle.load(open('logReg.pkl', 'rb'))
    pred = logReg.predict([[param1, param2, param3]])[0]
    if pred == 0:
        return "Email is spam"
    else:
        return "Email is valid"


@home.route('/logistic-regression-titanic')
@login_required
def logistic_regression_titanic():
    """
    We estimate the probabilities here
    """
    import pandas as pd
    import numpy as np
    train = pd.read_csv('titanic_train.csv')
    table = pd.DataFrame.from_csv("titanic_train.csv")
    data = table.to_html()#this works
    #print(data)
    return render_template('home/logistic-regression.html', tables=data, tabt=table, title='Admin dashboard')


