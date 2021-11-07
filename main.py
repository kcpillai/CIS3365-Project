import flask
import hashlib
from flask import jsonify
from flask import request, make_response
from sql import create_connection
from sql import execute_query
from mysql.connector import Error
import datetime
from datetime import datetime

# CREATE A STRING FOR THE CURRENT DATE
# FOUND FROM ONLINE SOURCE - https://www.tutorialspoint.com/How-to-store-and-retrieve-a-date-into-MySQL-database-using-Python
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')



app = flask.Flask(__name__) #  sets up the application
app.config["DEBUG"] = True #  allow to show errors in browser

# username is set as 'admin'
# password from apisecurity class, password is set as 'password'
masterPassword = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"



@app.route('/test', methods=['POST']) 
def test():
    conn = create_connection("CoT-CIS3365-09.cougarnet.uh.edu", --, --, "cis3368pqs")
    return 'Database Connection Worked!'


app.run()