from flask import Flask, render_template, request, session, redirect, url_for
import database_utils

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/test2")
def test2():
    return render_template("test2.html")


@app.route("/parentlogin", methods=['GET', 'POST'])
def parent_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verifylogin = database_utils.valid_parent_login(username, password)
        if verifylogin != -1:
            session['type'] = 'parent'
            session['id'] = verifylogin
            return url_for("parentschedule")
        else:
            return render_template("parentlogin.html")  # Failure to Login, Ginga
    else:
        return render_template("parentlogin.html")


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


@app.route("/teacherlogin", methods=['GET', 'POST'])
def teacher_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verifylogin = database_utils.valid_teacher_login(username, password)
        if verifylogin != -1:
            session['type'] = "teacher"
            session['id'] = verifylogin
            return url_for("teacherschedule")
        else:
            return render_template("teacherlogin.html")  # "Failure to login" Ginga Thing to Show This
    else:
        return render_template("teacherlogin.html")


@app.route("/teachercreate", methods=['GET', 'POST'])
def teacher_create():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email'].lower()
        school = request.form['school']
        if school == 'other':
            school = request.form['other_school']
        department = request.form['department']
        if department == 'other':
            department = request.form['other_department']
        room = request.form['room']
        result = database_utils.valid_create_teacher(username, password, repeat_password, first_name, last_name, email, school, department, room)
        if result[0]:
            return render_template("teacherlogin.html")  # result[1] Ginga Thing
        else:
            return render_template("teacher_create.html") # result[1] Ginga Thing
    else:
        return render_template("teachercreate.html")


@app.route("/parentselect", methods=['GET', 'POST'])
def parentselect():
    if 'type' in session and session['type'] == "parent":
        if request.method == 'POST':
            # Form Stuff
            return render_template("parentselect.html")
        else:
            # do stuff with session['id']
            return render_template("parentselect.html")
    else:
        return "Error, Something went wrong. Link to home" #NEEDS to create page


@app.route("/teacherschedule", methods=['GET', 'POST'])
def teacherschedule():
    if 'type' in session and session['type'] == "teacher":
        if request.method == 'POST':
            # Form Stuff
            return render_template("teacherschedule.html")
        else:
            # do stuff with session['id']
            return render_template("teacherschedule.html")
    else:
        return "Error, Something went wrong. Link to home" #Same page as method above

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Password"
    app.run(host='0.0.0.0', port=8000)
