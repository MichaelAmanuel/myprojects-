
from flask import Flask


app = Flask("yourapp")

#app = Flask(__name__)

@app.route("/")

def hello_word():
    return "<p>Hello, world!</p>"


@app.route("/hello") 
def viewfun():
    return "<p>Second Route</p>"


@app.route("/hello/bye")
def viewfun1():
    return "<h1>Third</h1>"

if __name__ == '__main__':
    app.run()
    