import flask
import hashlib
from flask import jsonify
from flask import request, make_response
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
from mysql import connector
import pyodbc
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

username = 'rdramir4'
password = '#HoneyB33z'
DB = 'cis3368pqs'
Connect = "DRIVER={{SQL Server}};SERVER=COT-CIS3365-09.cougarnet.uh.edu;DATABASE={};UID={};PWD={}".format(
    DB, username, password)
print('Connect')


app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True  # allow to show errors in browser


@app.route('/api/add', methods=['GET'])
def test():

    conn = pyodbc.connect(Connect)
    print("Connection to MySQL DB successful")
    my_cursor = conn.cursor()
    all_logs = "SELECT * FROM gender"
    my_cursor.execute = execute_read_query(Connect, all_logs)
    return jsonify(my_cursor)


@app.route('/test', methods=['POST']) 
def test():
    conn = create_connection("CoT-CIS3365-09.cougarnet.uh.edu", --, --, "cis3368pqs")
    return 'Database Connection Worked!'


app.run()
