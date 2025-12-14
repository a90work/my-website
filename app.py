from flask import Flask, request, redirect

app = Flask(__name__)

# اطلاعات کاربر (می‌تونی هرچقدر خواستی اضافه کنی)
users = {
    "ali@gmail.com": {
        "password": "1234",
        "page": "/ali"
    },
    "sara@gmail.com": {
        "password": "abcd",
        "page": "/sara"
    }
}

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if email in users and users[email]["password"] == password:
        return redirect(users[email]["page"])   # رفتن به صفحه مخصوص
    else:
        return "Invalid login!"

@app.route("/ali")
def ali_page():
    return "سلام علی! این صفحه مخصوص تو هست."

@app.route("/sara")
def sara_page():
    return "سلام سارا! این صفحه مخصوص تو هست."

@app.route("/")
def home():
    return "API is working!"

if __name__ == "__main__":
    app.run()
