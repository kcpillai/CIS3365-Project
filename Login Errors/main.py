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


app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True  # allow to show errors in browser

# username is set as 'admin'
# password from apisecurity class, password is set as 'password'
masterPassword = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"


conn = create_connection("CoT-CIS3365-09.cougarnet.uh.edu",
                         "cougarnet/kcpillai", "Patrick1*", "cis3368pqs")


@app.route('/api/addgender', methods=['POST'])  # creating the api using POST
def add_car():
    request_data = request.get_json()  # requesting the data from postman
    EmployeeID = request_data['EmployeeID']
    GenderName = request_data['GenderName']

    new_gender = "INSERT INTO gender(EmployeeID, GenderName) VALUES ('%s', '%s')" % (
        GenderName, EmployeeID)  # inserting the car into the car table
    execute_query(conn, new_gender)  # executing the query
    return 'Gender has been added'


app.run()
