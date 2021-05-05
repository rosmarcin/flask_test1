from flask import Flask, jsonify
from sqlite3 import connect, Error
import json

app = Flask(__name__)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
#    connect(db_file)

    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM PREDICTED_PATIENT_ENROLLMENT")

    rows = cur.fetchall()

    print(json.dumps(rows[1]))

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.route('/')
def index():
    return 'Hi! Server works!'


@app.route('/wellspring/api/v1/data', methods=['GET', 'POST', 'DELETE'])
def data_server():
# {
#      "entryDate": "string", 
#      "studyNumber": "string",
#      "patientsEnrolled": "number",
#      simulatedLaunchDate: "string",
#      case: "string",
#      lpi: "string",
#      targetLpi: "string",
#      targetEnrollment: "number",
#   }

# study number na poczatek 
# casy

    print('hello')
    return jsonify({'tasks': tasks})


if __name__=="__main__":
    database = "wellspring.db"
    conn = create_connection(database)
    with conn:
        print("2. Query all tasks")
        select_all_tasks(conn)


    app.run()