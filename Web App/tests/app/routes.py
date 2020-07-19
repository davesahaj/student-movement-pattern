from flask import render_template, request, jsonify, make_response
from app import app
import json
import pandas as pd


# Excel file to read
df = pd.read_excel('test.xlsx')

# preprocessing dataframe
df['Date'] = df['Date'].astype('datetime64[ns]')
df = df.sort_values(by='Date')

# location IDs
locations = ['Canteen', 'Hostel', 'CEP', 'LAB', 'RC', 'LT']

# Student IDs
students = df['Student ID'].unique()
students.sort()
# Dates list
dates = df['Date'].dt.date.unique()
dates.astype('datetime64[ns]')

# Date format for slider
date_mark = {i: dates[i] for i in range(0, len(dates))}
for i in date_mark:
    date_mark[i] = date_mark[i].strftime('%m/%d/%Y')
    date_mark[i] = date_mark[i][0:5]


# decorators
@app.route('/')
def home():
    #
    user = {'username': 'sahaj'}
    return render_template('basic_operations.html', student_ids=list(students), wifi_ids=json.dumps(locations))


@app.route("/locationwise", methods=["POST"])
def update_chart():

    req = request.get_json()
    print(req['wifi_id'])
    print(req['student_id'])

    

    res = make_response(jsonify(req), 200)

    return res
