from flask import Flask
from flask import render_template

HOST="localhost"
PORT=443

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host=HOST,port=PORT,debug=True)