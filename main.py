from flask import Flask, render_template, session, redirect, request
from  sqlite4  import  SQLite4

HOST="localhost"
PORT=443

database=SQLite4("database.db")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    database.create_table("chemy_info",["name",])

    app.run(host=HOST,port=PORT,debug=True)