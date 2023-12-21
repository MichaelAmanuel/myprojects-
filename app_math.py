

from flask import Flask


app = Flask("yourapp")

@app.route("/add", methods=['POST'])
def add():     
    a = request.json['a']
    b = request.json['b']
    return f"Sum: {int(a) + int(b)}"
    
@app.route("/add", methods=['POST'])
def subtract():
    a = request.json['a']
    b = request.json['b']
    return f"Subtraction: {int(a) - int(b)}"

@app.route("/add", methods=['POST'])
def multiply():
    a = request.json['a']
    b = request.json['b']
    return f"Multiplication: {int(a) * int(b)}"

@app.route("/add", methods=['POST'])
def divide():
    a = request.json['a']
    b = request.json['b']
    if y == 0:
        return "Division by zero is not allowed."
    return f"Division: {int(a) / int(b)}"
	
	
  
if __name__ == '__main__':
    app.run()