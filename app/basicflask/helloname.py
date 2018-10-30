from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "HELLO WORLD!!!"
@app.route("/hi/<name>")
def hello1(name):
    return "HELLO %s!!!" % name
if __name__ == "__main__":
    
    app.run(debug = True)
