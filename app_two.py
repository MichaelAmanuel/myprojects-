
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
    

@app.route("/add", method=['POST'])
def add():     
    a = request.json['a']
    b = request.json['b']
    return f"Sum: {x + y}"
    
@app.route("/subtract", method=['POST'])
def subtract():
    a = request.json['a']
    b = request.json['b']
    return f"Subtraction: {x - y}"

@app.route("/multiply", method=['POST'])
def multiply():
    a = request.json['a']
    b = request.json['b']
    return f"Multiplication: {x * y}"

@app.route("/divide", method=['POST'])
def divide():
    a = request.json['a']
    b = request.json['b']
    if y == 0:
        return "Division by zero is not allowed."
    return f"Division: {x / y}"



    
    
if __name__ == '__main__':
    app.run()
    