from flask import Flask, render_template, request, session, redirect, url_for
import database_utils

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/parentcreate", methods=['GET', 'POST'])
def parent_create():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email'].lower()
        result = database_utils.valid_create_parent(username, password, repeat_password, first_name, last_name, email)
        if result[0]:
            return result[1]
        else:
            return "Error:" + result[1]
    else:
        return render_template("parentcreate.html")


@app.route("/teachercreate", methods=['GET', 'POST'])
def teacher_create():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email'].lower()
        if (email == 'other'):
            email = request.form['other']
        school = request.form['school']
        department = request.form['department']
        room = request.form['room']
        result = database_utils.valid_create_teacher(username, password, repeat_password, first_name, last_name, email, school, department, room)
        if result[0]:
            return result[1]
        else:
            return "Error:" + result[1]
    else:
        return render_template("teachercreate.html")

if __name__== "__main__":
    app.debug = True
    app.secret_key = "Password"
    app.run(host='0.0.0.0', port=8000)
