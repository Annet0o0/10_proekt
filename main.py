from flask import Flask, render_template, redirect, request
from sqlite4 import SQLite4

HOST="localhost"
PORT=443

CHYM=[
    ("Хлориды","Cl⁻"),
    ("Бромиды","Br⁻"),
    ("Фториды","А⁻"),
    ("Сульфаты","SO₄²⁻"),
    
    ("Бор","B"),
    ("Натрий","Na"),
    ("Магний","Mg"),
    ("Кальций","K"),
    ("Калий","Ca"),
    ("Стронций","Sr"),
    ("Свинец","Pl"),
    ("Цинк","Zn"),
    ("Железо","Fe"),
    ("Марганец","Mn"),
    ("Медь","Cu")
]

database=SQLite4("database.db")
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/data")
def data():
    info=database.select("info")
    return render_template("data.html",info=info,size=len(info))

if __name__=="__main__":
    database.connect()
    database.create_table("info",["name","good","ph","petroleum","cl","br","f","so","b","na","mg","ca","k","sr","pl","zn","fe","mn","cu"])

    #Default info
    if len(database.select("info"))==0: database.insert("info",
    {
        "name":"Вишера",
        "good":10,
        "ph":1,
        "petroleum":0.5,
        "cl":0.5,
        "br":0.5,
        "f":0.5,
        "so":0.5,
        "b":0.5,
        "na":0.5,
        "mg":0.5,
        "ca":0.5,
        "k":0.5,
        "sr":0.5,
        "pl":0.5,
        "zn":0.5,
        "fe":0.5,
        "mn":0.5,
        "cu":0.5
    })

    app.run(host=HOST,port=PORT,debug=True)