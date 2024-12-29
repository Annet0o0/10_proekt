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
    if len(database.select("chemy_info"))==0: database.insert("chemy_info",
    {
        "name":"Вишера",
        "good":10,
        "ph":1,
        "petroleum":0.5,
        "hloris":0.5,
        "sulfis":0.5,
        "bromis":0.5,
        "ftoris":0.5,
        "boris":0.5,
        "natris":0.5,
        "magnis":0.5,
        "calcis":0.5,
        "kalis":0.5,
        "stroncis":0.5,
        "plumbus":0.5,
        "zincum":0.5,
        "ferrum":0.5,
        "manganum":0.5,
        "cuprum":0.5
    })

    app.run(host=HOST,port=PORT,debug=True)