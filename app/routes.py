from flask import render_template, request, jsonify, make_response
from app import app
import json
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient

###############################
#   PREPROCESSING FUNCTIONS   #
###############################


def findFrequency(lid, sid):

    fl = df.loc[(df['Wifi Id'] == lid) & (df['Student ID'] == sid)]    
    freq = len(fl.index)
    return (freq)

def findWeekday(sid):
    count = -1
    result = []
    tmp = df.loc[df['Student ID'] == sid]

    for lid in locations:
        result.append([])
        count = count+1
        print(result)

        x = tmp.loc[df['Wifi Id'] == lid]
        for wid in weekdays:
            result[count].append(len((x.loc[x['weekday'] == wid].index))) 
            

    

    return (result)

def findWeekdayLocation( lid):
    count = -1
    result = []
    tmp = df.loc[df['Wifi Id'] == lid]
    for wid in weekdays:
        result.append(len((tmp.loc[tmp['weekday'] == wid].index))) 


    return result

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


#Atlas Connection
#cluster = MongoClient("mongodb+srv://manav:manav1234@cluster0-b4jm1.mongodb.net/Data?retryWrites=true&w=majority")
#db = cluster.Data
#collection = db.Final
#df = pd.DataFrame(list(collection.find()))
print("Database fetched")

# preprocessing dataframe
df['Date'] = df['Date'].astype('datetime64[ns]')
#df = df.sort_values(by='Date')
df['weekday'] = df['Date'].map(get_weekday)

# locations IDs
locations = ['Canteen', 'Hostel', 'CEP', 'LAB', 'RC', 'LT']

# Days IDs
weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

# Student IDs
students = df['Student ID'].unique()
students.sort()

# students_tmp = []
# for i in students:
#     students_tmp.append(i)

# Dates list
dates = df['Date'].dt.date.unique()
dates.astype('datetime64[ns]')


# # Date format for slider
# date_mark = {i: dates[i] for i in range(0, len(dates))}
# for i in date_mark:
#     date_mark[i] = date_mark[i].strftime('%m/%d/%Y')
#     date_mark[i] = date_mark[i][0:5]

print("Data Preprocessed")

#test#


# endtest


# decorators

print("Server Started")
@app.route('/')
def home():
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
        y_data = findWeekday(int(req['student_id']))
          
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
        y_data = findWeekdayLocation( req['wifi_id'])
        
        print(y_data)

        res_data = [x_data, y_data]
        res = make_response(jsonify(res_data), 200)

        return res


@app.route("/weekdaywise", methods=["POST"])
def updateWeekdayChart():
    print("NULL")