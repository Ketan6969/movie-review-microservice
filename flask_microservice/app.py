from flask import Flask, request, jsonify
import mysql
import mysql.connector

app = Flask('__name__')
def connect_db():
    return mysql.connector.connect(host = 'localhost', user = 'root', password = 'tiger', database = 'test')

@app.route("/getall", methods=['GET'])
def addemp():
    db = connect_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM test')
    result = cur.fetchall()
    cur.close()
    db.close()
    return jsonify(result)

@app.route('/')
def home():
    return f'<h1>Welcome to homepage!!<h1>'

# @app.route('/sign_up', methods = ['POST'])
# def add_emp():
#     db = connect_db()
#     cur = db.cursor()
#     cur.execute('insert into test')
if __name__ == "__main__":
    app.run(debug=True)
