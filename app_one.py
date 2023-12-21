
from flask import Flask


app = Flask("yourapp")

#app = Flask(__name__)

@app.route("/")

def hello_word():
    return "<p>Hello, world!</p>"



if __name__ == '__main__':
    app.run()
    