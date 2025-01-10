from flask import Flask, render_template, request, make_response
from sqlite4 import SQLite4
from secrets import token_urlsafe

HOST="localhost"
PORT=443

PASSWORD="isufiubns3gw73gy3cpohowfyp89yal4ghohd;af'lsdfasdkma'sdmdsvsdvnsmd98487wy424t8"

CHYM=[
    ("Хлориды","Cl⁻"),
    ("Бромиды","Br⁻"),
    ("Фториды","F⁻"),
    ("Сульфаты","SO₄²⁻"),
    
    ("Бор","B"),
    ("Натрий","Na"),
    ("Магний","Mg"),
    ("Кальций","Ca"),
    ("Калий","K"),
    ("Стронций","Sr"),
    ("Свинец","Pb"),
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
    return render_template("data.html",info=info,info_size=len(info),chym=CHYM,chym_range=range(len(CHYM)))

sessions:dict[str,bool]={}

@app.get("/editor")
def editor():
    session=request.cookies.get("session")

    if session and sessions.get(session): return render_template("edit.html")
    return new_editor_session_resp()

@app.post("/editor")
def editor_forms():
    session=request.cookies.get("session")

    if not session: return new_editor_session_resp()
    sess=sessions.get(session)

    if sess==None: return new_editor_session_resp()

    if sess:
        pass
    else:
        passinput=request.form["pass-input"]
        if passinput==PASSWORD:
            sessions[session]=True
            return render_template("edit.html")
        else: return render_template("edit_auth.html",error="Неверный пороль"), 401
        

def new_editor_session_resp():
    new_session=token_urlsafe(256)
    sessions[new_session]=False
    
    resp=make_response(render_template("edit_auth.html"))
    resp.set_cookie("session",new_session,httponly=True)
    return resp


if __name__=="__main__":
    database.connect()
    database.create_table("info",["name","good","ph","petroleum","cl","br","f","so","b","na","mg","ca","k","sr","pb","zn","fe","mn","cu"])

    #Default info
    if len(database.select("info"))==0: 
        database.insert("info",{
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
            "pb":0.5,
            "zn":0.5,
            "fe":0.5,
            "mn":0.5,
            "cu":0.5
        })
        database.insert("info",{
            "name":"Смолишена",
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
            "pb":0.5,
            "zn":0.5,
            "fe":0.5,
            "mn":0.5,
            "cu":0.5
        })

    app.run(host=HOST,port=PORT)