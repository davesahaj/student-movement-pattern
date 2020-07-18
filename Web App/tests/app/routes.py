from flask import render_template, request, jsonify, make_response
from app import app
import json
import pandas as pd


@app.route('/')
def home():

    user = {'username': 'sahaj'}
    return render_template('basic_operations.html', title='Home', user=user)


@app.route('/sum', methods=['POST'])
def sum_num():
    print("Sum function")
    rf = request.form
    print(rf)
    for key in rf.keys():
        data = key
    print(data)
    data_dic = json.loads(data)
    print(data_dic.keys())
    sum_data = data_dic['sum']
    sumd = 0
    for _ in sum_data:
        sumd += _
    resp_dic = {'sum': sumd, 'msg': 'Sum performed'}
    resp = jsonify(resp_dic)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
