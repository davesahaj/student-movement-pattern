from flask import render_template, request, jsonify, make_response
from app import app
import json
import pandas as pd
import numpy as np

###############################
#   PREPROCESSING FUNCTIONS   #
###############################


def findFrequency(lid, sid):
    fl = df.loc[df['Wifi Id'] == lid]
    fl = fl.loc[fl['Student ID'] == sid]
    
    freq = fl.index
    freq = len(freq)
    return (freq)


def findWeekday(wid, lid, sid):
    tmp = df
    tmp['weekday'] = tmp['Date'].map(get_weekday)
    tmp = tmp.loc[df['Wifi Id'] == lid]
    tmp = tmp.loc[tmp['Student ID'] == sid]
    tmp = tmp.loc[tmp['weekday'] == wid]
    freq = tmp.index
    freq = len(freq)
    print(str(freq) + " " + wid+" "+lid)

    return (freq)

def findWeekdayLocation(wid, lid):
    tmp = df
    tmp['weekday'] = tmp['Date'].map(get_weekday)
    tmp = tmp.loc[df['Wifi Id'] == lid]
    tmp = tmp.loc[tmp['weekday'] == wid]
    freq = tmp.index
    freq = len(freq)
    print(str(freq) + " " + wid+" "+lid)

    return (freq)


def get_dom(dt):
    return dt.day


def get_weekday(dt):
    return dt.day_name()


def get_date(dt):
    return dt.date()


def get_hour(dt):
    return dt.hour


def get_minute(dt):
    return dt.minute
###############################


# Excel file to read
df = pd.read_excel('test.xlsx')

# preprocessing dataframe
df['Date'] = df['Date'].astype('datetime64[ns]')
df = df.sort_values(by='Date')

# locations IDs
locations = ['Canteen', 'Hostel', 'CEP', 'LAB', 'RC', 'LT']

# Days IDs
weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

# Student IDs
students = df['Student ID'].unique()
students.sort()

students_tmp = []
for i in students:
    students_tmp.append(i)

# Dates list
dates = df['Date'].dt.date.unique()
dates.astype('datetime64[ns]')


# Date format for slider
date_mark = {i: dates[i] for i in range(0, len(dates))}
for i in date_mark:
    date_mark[i] = date_mark[i].strftime('%m/%d/%Y')
    date_mark[i] = date_mark[i][0:5]


#test#


# endtest


# decorators
@app.route('/')
def home():

    user = {'username': 'sahaj'}
    return render_template('basic_operations.html', student_ids=list(students), wifi_ids=json.dumps(locations))


@app.route("/studentwise", methods=["POST"])
def updateStudentChart():

    req = request.get_json()
    print(req['student_id'])
    print(req['filter'])

    if req['filter'] == 'location':
        x_data = locations
        y_data = []

        for wifi in x_data:
            y_data.append(findFrequency(wifi, int(req['student_id'])))

        res_data = [x_data, y_data]
        res = make_response(jsonify(res_data), 200)

        return res

    if req['filter'] == 'weekdays':
        x_data = weekdays
        y_data = []

        tmp = []

        for wifi in locations:
            for day in x_data:
                tmp.append(findWeekday(day, wifi, int(req['student_id'])))
            y_data.append(tmp)
            tmp = []

        print(y_data)

        res_data = [x_data, y_data]
        res = make_response(jsonify(res_data), 200)

        return res


@app.route("/locationwise", methods=["POST"])
def updateLocationChart():

    req = request.get_json()
    print(req['wifi_id'])
    print(req['filter'])

    if req['filter'] == 'students':
        x_data = students.tolist()
        y_data = []

        for student in x_data:
            y_data.append(findFrequency(req['wifi_id'], student))

        print(x_data)
        print(y_data)

        res_data = [x_data, y_data]
        res = make_response(jsonify(res_data), 200)

        return res

    if req['filter'] == 'weekdays':
        x_data = weekdays
        y_data = []

        tmp = []


        for day in x_data:
            tmp.append(findWeekdayLocation(day, req['wifi_id']))
        y_data.append(tmp)
        tmp = []

        print(y_data)

        res_data = [x_data, y_data]
        res = make_response(jsonify(res_data), 200)

        return res


@app.route("/weekdaywise", methods=["POST"])
def updateWeekdayChart():

    req = request.get_json()
    print(req['student_id'])
    print(req['filter'])

    if req['filter'] == 'location':
        x_data = locations
        y_data = []

        for wifi in x_data:
            y_data.append(findFrequency(wifi, int(req['student_id'])))

        res_data = [x_data, y_data]
        res = make_response(jsonify(res_data), 200)

        return res

    if req['filter'] == 'weekdays':
        x_data = weekdays
        y_data = []

        tmp = []

        for wifi in locations:
            for day in x_data:
                tmp.append(findWeekday(day, wifi, int(req['student_id'])))
            y_data.append(tmp)
            tmp = []

        print(y_data)

        res_data = [x_data, y_data]
        res = make_response(jsonify(res_data), 200)

        return res
