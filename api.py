
import flask
from flask import jsonify, request, render_template
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False


rawdata = pd.read_csv("1_rawdata.csv")
rawdata_list = []
nrows = rawdata.shape[0]


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/get_all', methods=['GET'])
def rawdata_all():
    return render_template('tables.html', tables=[rawdata.to_html(classes='data')], titles=rawdata.columns.values)


@app.route('/new_user', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']

app.run()