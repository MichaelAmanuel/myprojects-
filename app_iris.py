



from flask import Flask


app = Flask("yourapp")

@app.route("/add", methods=['POST'])
def add():     
    a = request.json['a']
    b = request.json['b']
    return f"Sum: {int(a) + int(b)}"
    
@app.route("/iris", methods=['POST'])
def classify():
    a = request.json['a']
    b = request.json['b']
    c = request.json['c']
    d = request.json['d']
    loaded_model = pickle.load(open("model.pkl", "rb"))
    test = np.array([a, b, c, d])
    return f"Sum: {int(a) + int(b)}"
	
	
  
if __name__ == '__main__':
    add.run()