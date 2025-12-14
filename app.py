from flask import Flask, request, redirect, render_template

app = Flask(__name__)

users = {
    "asr@gmail.com": {"password": "1390", "page": "asr.html"},
    "family@gmail.com": {"password": "58629097", "page": "family.html"}
}

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if email in users and users[email]["password"] == password:
        return render_template(users[email]["page"])
    else:
        return "Invalid login!"
