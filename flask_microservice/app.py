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
    return jsonify(result )

@app.route('/add_entry', methods=['POST'])
def add_entry():
    # Get data from request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Insert into the database
    db = connect_db()
    cur = db.cursor()
    query = "INSERT INTO test (email, password) VALUES (%s, %s)"
    values = (username, password)
    cur.execute(query, values)
    db.commit()

    # Get the ID of the newly added entry
    entry_id = cur.lastrowid

    cur.close()
    db.close()

    return jsonify({'message': 'Entry added successfully', 'id': entry_id}), 201


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
