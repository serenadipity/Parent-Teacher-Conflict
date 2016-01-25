from flask import Flask, render_template, request, session, redirect, url_for
import database_utils, utils

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/error")
def error():
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
            return redirect("parentselect")
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
            return render_template("parentcreate.html", error=True, message=message)
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
            return render_template("teacherlogin.html", error=True)
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
        return render_template("teachercreate.html", schools=school_list)


@app.route("/parentselect")
def parentselect():
    if 'type' in session and session['type'] == "parent":
        session['step'] = 0
        step = session['step']
        school_list = database_utils.get_schools()
        return render_template("parentselect.html", view = False, title = "Find Your Teacher", step = step, schools=school_list)
    else:
        return redirect("error")


@app.route("/findTeachers", methods=['POST'])
def findTeachers():
    if request.method == 'POST' and 'type' in session and session['type'] == "parent" and 'id' in session:
        date = request.form['date']
        school = request.form['school']
        availableTeachers = database_utils.get_all_available(date, school)
        session['step'] = 1
        step = session['step']
        session['date'] = date
        return render_template("parentselect.html", view = False, title = "Choose Your Teacher", step = step, teachers=availableTeachers)
    else:
        return redirect("error")


@app.route("/findAppointments", methods=['POST'])
def findAppointments():
    if request.method == 'POST' and 'type' in session and session['type'] == "parent" and 'id' in session:
        teachers = request.form.getlist('teachers')
        print teachers
        date = session['date']
        time = database_utils.get_time(date)
        teacherschedules = {}
        for teacher in teachers:
            teacherschedules[teacher] = database_utils.get_teacher_name(teacher) + database_utils.get_teacher_appointments(teacher, date)
        tablestring = utils.thingToDo(teacherschedules, date, time)
        session['step'] = 2
        step = session['step']
        return render_template("parentselect.html", view = False, title = "Choose Your Appointment Time",  step = step, appointments=tablestring)
    else:
        return redirect("error")


@app.route("/parentScheduleAppointments", methods=['POST'])
def parentscheduleappointments():
    if request.method == 'POST' and 'type' in session and session['type'] == 'parent' and 'id' in session:
        PID = session['id']
        date = request.form['date']
        time = request.form['time']
        for i in range(50):
            TID = request.form[str(i)]
            if TID != "-1":
                database_utils.make_appointment(PID, TID, date, time, i)
        return redirect("parentschedule")
    else:
        return redirect("error")
    

@app.route("/parentschedule", methods=['GET', 'POST'])
def parentschedule():
    if 'type' in session and session['type'] == "parent":
        if request.method == 'POST':
            parent_id = session['id']
            date = request.form['date']
            appointments = database_utils.get_parent_appointments(parent_id, date)
            tablestring = utils.createSchedule(appointments)
            return render_template("parentselect.html", view = True, title = "Here are Your Appointments", appointment=tablestring)
        elif 'date' in session:
            date = session['date']
            PID = session['id']
            appointments = database_utils.get_parent_appointments(PID, date)
            tablestring = utils.createSchedule(appointments)
            return render_template("parentselect.html", view = True,  title = "Here are Your Appointments", appointment=tablestring)
        else:
            return redirect("error")
    else:
        return redirect("error")


@app.route("/teacherschedule", methods=['GET', 'POST'])
def teacherschedule():
    if 'type' in session and session['type'] == "teacher":
        if request.method == 'POST':
            teacher_id = session['id']
            date = request.form['date']
            appointments = database_utils.get_teacher_appointments(teacher_id, date)
            tablestring = utils.createSchedule(appointments)
            print tablestring
            return render_template("teacherschedule.html", appointment=tablestring)
        else:
            return render_template("teacherschedule.html")
    else:
        return redirect("error")


@app.route("/addavailability", methods=['POST'])
def addavailability():
    if request.method == 'POST' and 'type' in session and session['type'] == "teacher" and 'id' in session:
        teacher_id = session['id']
        date = request.form['date']
        time = request.form['time']
        database_utils.set_teacher_availability(teacher_id, date, time)
        return redirect("teacherschedule")
    else:
        return redirect("error")


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Password"
    app.run(host='0.0.0.0', port=8000)
