from flask import Flask, url_for, session, render_template, request, redirect
import json

app = Flask(__name__)
app.secret_key = "PyFlask_2k18_1516"

@app.route("/", methods = ["GET"])
def index():

    if("loggedIn" in session.keys() and session["loggedIn"] == True):
        return redirect("/dashboard"), 302
    
    return render_template("index.html"), 200

@app.route("/login", methods = ["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    loginData = open("data/user.json", "r+")
    jsonData = loginData.read()
    loginData.close()
    print(jsonData)

    if jsonData is not "":

        dataDictionary = json.loads(jsonData)
        if username in dataDictionary.keys() and dataDictionary[username] == password:
            session["loggedIn"] = True
            session["username"] = username
            return redirect(url_for("dashboard"), 302)

        elif username in dataDictionary.keys() and dataDictionary[username] is not password:
            return render_template("index.html", message = "Invalid Username/Password", error = True)
        
        else:
            dataDictionary[username] = password
            loginData = open("data/user.json", "w+")
            loginData.write(json.dumps(dataDictionary))
            loginData.close()
            return render_template("index.html", message = "Successful Signup", error = False)
            
    else:
        jsonData = {username:password}
        loginData = open("data/user.json", "w+")
        loginData.write(json.dumps(jsonData))
        loginData.close()
        return render_template("index.html", message = "Successful Signup", error = False)


@app.route("/dashboard", methods = ["GET"])
def dashboard():
    if("loggedIn" in session.keys() and session["loggedIn"] is not True):
        return render_template("index.html", message = "Unauthorized", error = True), 401
    return render_template("dashboard.html")

@app.route("/addnote", methods = ["POST"])
def addnote():
    if("loggedIn" in session.keys() and session["loggedIn"] is not True):
        return render_template("index.html", message = "Unauthorized", error = True), 401
    title = request.form["title"]
    note = request.form["note"]
    username = session["username"]
    notesData = open("data/notes.json", "r+")
    jsonData = notesData.read()
    notesData.close()
    notesData = open("data/notes.json", "w+")
    if jsonData is not "":
        notes = json.loads(jsonData)
        if username not in notes.keys():
            notes[username] = {}
        if title not in notes[username].keys():
            notes[username][title] = note
            notesData.write(json.dumps(notes))
            notesData.close()
            return render_template("dashboard.html", message = "Note added successfully", error = False), 201
        else:
            notes = json.loads(jsonData)
            notesData.write(json.dumps(notes))
            notesData.close()
            return render_template("dashboard.html", message = "Note with title '{}', already exists".format(title), error = True)
    else:
        notes = {username:{title: note}}
        notesData.write(json.dumps(notes))
        notesData.close()
        return render_template("dashboard.html", message = "Note added successfully", error = False), 201

@app.route("/getnotes", methods = ["GET"])
def getnotes():
    if("loggedIn" in session.keys() and session["loggedIn"] is not True):
        return render_template("index.html", message = "Unauthorized", error = True), 401
    notesData = open("data/notes.json", "r+")
    jsonData = notesData.read()
    notesData.close()
    if jsonData is not "":
        notes = json.loads(jsonData)
        if session["username"] not in notes.keys():
            return render_template("notes.html", notes = {}, message = "No notes added yet", error = True)
        return render_template("notes.html", notes = notes[session["username"]])
    else:
        return render_template("notes.html", notes = {}, message = "No notes added yet", error = True)

@app.route("/logout", methods = ["GET"])
def logout():
    if("loggedIn" in session):
        del session["loggedIn"]
        del session["username"]
    return redirect("/"), 302


if __name__ == "__main__":
    app.run("127.0.0.1", "3004", debug = True)