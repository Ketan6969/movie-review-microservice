from flask import Flask, request

app = Flask('__name__')

@app.route('/')
def home():
    return f'<h1>Welcome to homepage!!<h1>'

if __name__ == "__main__":
    app.run(debug=True)
