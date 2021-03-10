import flask
from flask import request, render_template
import pandas as pd
import numpy as np


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

rawdata = pd.read_csv("1_rawdata.csv")
rawdata_list = []
nrows = rawdata.shape[0]
headers = rawdata.columns.values[1:-1]


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/get_all', methods=['GET'])
def rawdata_all():
    return render_template('tables.html', table=rawdata.to_html(classes='data'), titles=headers)


@app.route('/get_custom', methods=['GET', 'POST'])
def custom_rawdata():
    columns = []
    if request.method == 'GET':
        list_ids = get_column_values_from_table(header="PlaybrushID", datasource=rawdata)
        return render_template('custom.html', tables=[rawdata.to_html(classes='data')], titles=headers,
                               list_ids=list_ids)

    if request.method == 'POST':
        get_id = request.form.get("playbrushid")
        get_columns = rawdata.query(f"PlaybrushID=='{get_id}'")

        for header in headers:
            if request.form.get(header):
                columns.append(header)
        result = get_columns.filter(items=columns)
        return render_template('tables.html', table=result.to_html(classes='data'), titles=headers)


@app.route('/new_user', methods=['POST'])
def submit():
    return render_template('new_user.html')


def get_column_values_from_table(header, datasource):
    column_values = getattr(datasource, header)
    return set(column_values.values)
