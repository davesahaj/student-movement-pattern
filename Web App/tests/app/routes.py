from flask import render_template, request, jsonify, make_response
from app import app
import json
import pandas as pd


@app.route('/')
def home():
    df = pd.read_excel('test.xlsx')
    df['Date'] = df['Date'].astype('datetime64[ns]')
    df = df.sort_values(by='Date')

    #locations = df['Wifi Id'].unique()
    locations = ['"Canteen"', '"Hostel"', '"CEP"', '"LAB"', '"RC"', '"LT"']
    students = df['Student ID'].unique()
    dates = df['Date'].dt.date.unique()
    dates.astype('datetime64[ns]')

    user = {'username': 'sahaj'}
    return render_template('basic_operations.html', title='Home', user=user)


@app.route("/home")
def guestbook():

    return render_template("basic_operations.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()
    print(req)

    res = make_response(jsonify(req), 200)

    return res
