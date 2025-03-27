from flask import Flask, render_template, request, make_response
from sqlite4 import SQLite4
from secrets import token_urlsafe
import re

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

keys:list[str]
keys_count:int

database=SQLite4("database.db")
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/data")
def data():
    info=list(map(lambda x:x[1::],database.select("info")))
    return render_template("data.html",info=info,info_size=len(info),chym=CHYM,chym_range=range(len(CHYM)))

sessions:dict[str,bool]={}

@app.get("/editor")
def editor():
    session=request.cookies.get("session")

    if session and sessions.get(session): return editor_resp()
    return new_editor_session_resp()

@app.post("/editor")
def editor_forms():
    session=request.cookies.get("session")

    if not session: return new_editor_session_resp()
    sess=sessions.get(session)

    if sess==None: return new_editor_session_resp()

    if sess:
        ls:list[list[str]]=[]

        for key in request.form.keys():
            try:
                if re.fullmatch("base-[0-9]+-[0-9]+",key):
                    vals=key.split('-')
                    fill_to(ls,int(vals[1]),int(vals[2]),float(request.form.get(key)))
                elif re.fullmatch("chym-[0-9]+-[0-9]+",key):
                    vals=key.split('-')
                    fill_to(ls,int(vals[1]),int(vals[2])+4,float(request.form.get(key)))
                elif re.fullmatch("name-[0-9]+",key):
                    vals=key.split('-')
                    fill_to(ls,int(vals[1]),0,request.form.get(key))
            except ValueError:
                return "Incorrect form", 422
            
        size=len(ls)
        curr_size=len(database.select("info"))

        if size>curr_size:
            for i in range(curr_size,size): database.insert("info",{"id":i})
        elif size<curr_size:
            for i in range(size,curr_size): database.delete("info","id=="+str(i))

        for i in range(size):
            mp={}
            sub=ls[i]
            for j in range(keys_count):
                mp[keys[j]]=sub[j]
            database.update("info",mp,"id=="+str(i))

        return editor_resp()
    else:
        passinput=request.form["pass-input"]
        if passinput==PASSWORD:
            sessions[session]=True
            return editor_resp()
        else: return render_template("edit_auth.html",error="Неверный пороль")

@app.route("/editor/js")
def editor_js():
    session=request.cookies.get("session")

    if not session: return "Not accessed", 401
    sess=sessions.get(session)

    if sess:
        resp=make_response(render_template("edit.js",chym_size=len(CHYM)))
        resp.content_type="text/javascript; charset=utf-8"
        return resp
    else: return "Not accessed", 401

@app.route("/editor/css")
def editor_css():
    session=request.cookies.get("session")

    if not session: return "Not accessed", 401
    sess=sessions.get(session)

    if sess:
        resp=make_response(render_template("edit.css"))
        resp.content_type="text/css; charset=utf-8"
        return resp
    else: return "Not accessed", 401

def fill_to(ls:list[list[str]],i:int,j:int,value):
    size=len(ls)
    if i >= size:
        for index in range(i-size+1): ls.append([])
        size=i+1
    ls2=ls[i]
    size_ls2=len(ls2)

    if j>=size_ls2:
        for index in range(j-size_ls2+1): ls2.append(None)
        size_ls2=j+1
    
    ls2[j]=value
        

def new_editor_session_resp():
    new_session=token_urlsafe(256)
    sessions[new_session]=False
    
    resp=make_response(render_template("edit_auth.html"))
    resp.set_cookie("session",new_session,httponly=True)
    return resp

def editor_resp():
    info=list(map(lambda x:x[1::],database.select("info")))
    return render_template("edit.html",info=info,info_size=len(info),info_range=range(len(info)),chym=CHYM,chym_size=len(CHYM),chym_range=range(len(CHYM)))


if __name__=="__main__":
    database.connect()
    database.create_table("info",[
        "id INTEGER PRIMARY KEY",
        "name TEXT",
        "good INTEGER",
        "ph REAL",
        "petroleum REAL",
        "cl REAL",
        "br REAL",
        "f REAL",
        "so REAL",
        "b REAL",
        "na REAL",
        "mg REAL",
        "ca REAL",
        "k REAL",
        "sr REAL",
        "pb REAL",
        "zn REAL",
        "fe REAL",
        "mn REAL",
        "cu REAL"
    ])

    keys=keys=list(map(lambda x: x[1],database.connection.execute("PRAGMA table_info(info)").fetchall()[1::]))
    keys_count=len(keys)

    app.run(host=HOST,port=PORT,ssl_context='adhoc')