from flask import Flask, render_template, request, session, redirect, url_for
import database_utils

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/test2")
def test2():
    return render_template("error.html")


@app.route("/parentlogin", methods=['GET', 'POST'])
def parent_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verifylogin = database_utils.valid_parent_login(username, password)
        if verifylogin != -1:
            session['type'] = 'parent'
            session['id'] = verifylogin
            return redirect("parentschedule")
        else:
            return render_template("parentlogin.html", error=True)
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
            return redirect("parentlogin")
        else:
            message = result[1]
            return render_template("parentcreate.html",error = True, message = message)
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
            return redirect("teacherschedule")
        else:
            return render_template("teacherlogin.html", error = True)  # "Failure to login" Ginga Thing to Show This
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
        if (school == "other"):
            school = request.form['other']
        room = request.form['room']
        result = database_utils.valid_create_teacher(username, password, repeat_password, first_name, last_name, email, school, room)
        if result[0]:
             return redirect("teacherlogin")
        else:
            message = result[1]
            school_list = database_utils.get_schools()
            return render_template("teachercreate.html", schools = school_list, error = True, message = message) # result[1] Ginga Thing
    else:
        school_list = database_utils.get_schools()
        return render_template("teachercreate.html", schools = school_list)


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


@app.route("/addavailability", methods=['POST'])
def addavailability():
    if request.method == 'POST' and 'type' in session and session['type'] == "teacher" and id in session:
        teacher_id = session['id']
        date = request.form['date']
        time = request.form['time']
        if time = 'afternoon':
            sections = 
        else:
            sections =
        database_utils.set_teacher_availability(teacher_id, date, time, sections)
        return redirect("teacherschedule")
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Password"
    app.run(host='0.0.0.0', port=8000)
