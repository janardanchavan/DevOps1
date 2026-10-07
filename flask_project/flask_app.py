from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/country')
def country():
    return "Country: India"

@app.route('/city')
def city():
    return "City: Bangalore"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

