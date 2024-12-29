from flask import Flask, render_template, redirect, request
from sqlite4 import SQLite4

HOST="localhost"
PORT=443

database=SQLite4("database.db")
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/data")
def data():
    return render_template("data.html",data=database.select("chemy_info"))

if __name__=="__main__":
    database.connect()
    database.create_table("chemy_info",["name","good","ph","petroleum","hloris","sulfis","bromis","ftoris","boris","natris","magnis","calcis","kalis","stroncis","plumbus","zincum","ferrum","manganum","cuprum"])

    app.run(host=HOST,port=PORT,debug=True)