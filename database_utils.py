import sqlite3  # Database

from hashlib import sha512  # Hashing for Passwords
from uuid import uuid4  # Salting for Passwords

import utils  # Minor Utilities


# Parent Database -------------------------------------------------------------------------------------------------------------------------------------------
"""
Parent Database - Stores parents login information
+-----------+----------+----------+------+------------+-----------+-------+
| Parent_ID | Username | Password | Salt | First Name | Last Name | Email |
+-----------+----------+----------+------+------------+-----------+-------+
| INT       | TEXT     | INT      | INT  | TEXT       | TEXT      | TEXT  |
+-----------+----------+----------+------+------------+-----------+-------+
"""


# Validates a parent logging in
# Returns an int
# -1 if failed, Parent Id if successful
def valid_parent_login(username, password):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "parent_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return -1
    q = 'SELECT password, salt FROM parent_database WHERE username = ?'
    pepper_and_salt = c.execute(q, (username,)).fetchone()
    if pepper_and_salt and sha512((password + pepper_and_salt[1]) * 10000).hexdigest() == pepper_and_salt[0]:
        q = "SELECT parent_id FROM parent_database WHERE username = ?"
        id = c.execute(q, (username,)).fetchone()
        conn.close()
        return id[0]
    conn.close()
    return -1


# Adds a parent to the database
# Returns a list [Boolean, String]
# True if successful, False if unsuccessful
# String is a status message# Adds a parent to the database
# Returns a list [Boolean, String]
# True if successful, False if unsuccessful
# String is a status message
def valid_create_parent(username, password, repeat_password, first_name, last_name, email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'CREATE TABLE IF NOT EXISTS parent_database (parent_id INT, username TEXT, password INT, salt INT, first_name TEXT, last_name TEXT, email TEXT)'
    c.execute(q)
    q = 'SELECT username, email FROM parent_database'
    users = c.execute(q)
    valid_data = utils.valid_data(username, password, repeat_password, email, users)
    if not valid_data[0]:
        conn.close()
        return valid_data
    else:
        salt = uuid4().hex
        hash_password = sha512((password + salt) * 10000).hexdigest()
        q = 'SELECT COUNT(*) FROM parent_database'
        num_rows = c.execute(q).fetchone()[0]
        q = 'INSERT INTO parent_database (parent_id, username, password, salt, first_name, last_name, email) VALUES (?, ?, ?, ?, ?, ?, ?)'
        c.execute(q, (num_rows + 1, username, hash_password, salt, first_name, last_name, email))
        conn.commit()
        conn.close()
        return [True, "Successful Account Creation"]


# Teacher Database ------------------------------------------------------------------------------------------------------------------------------------------
"""
Teacher Database - Stores parents login information
+------------+----------+----------+------+------------+-----------+-------+--------+------+
| Teacher_ID | Username | Password | Salt | First Name | Last Name | Email | School | Room |
+------------+----------+----------+------+------------+-----------+-------+--------+------+
| INT        | TEXT     | INT      | INT  | TEXT       | TEXT      | TEXT  | TEXT   | TEXT |
+------------+----------+----------+------+------------+-----------+-------+--------+------+
"""


def valid_teacher_login(username, password):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "teacher_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return -1
    q = 'SELECT password, salt FROM teacher_database WHERE username = ?'
    pepper_and_salt = c.execute(q, (username,)).fetchone()
    if pepper_and_salt and sha512((password + pepper_and_salt[1]) * 10000).hexdigest() == pepper_and_salt[0]:
        q = "SELECT teacher_id FROM teacher_database WHERE username = ?"
        id = c.execute(q, (username,)).fetchone()
        conn.close()
        return id[0]
    conn.close()
    return -1


def valid_create_teacher(username, password, repeat_password, first_name, last_name, email, school, room):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'CREATE TABLE IF NOT EXISTS teacher_database (teacher_id INT, username TEXT, password INT, salt INT, first_name TEXT, last_name TEXT, email TEXT, school TEXT, room TEXT)'
    c.execute(q)
    q = 'SELECT username, email FROM teacher_database'
    users = c.execute(q)
    valid_data = utils.valid_data(username, password, repeat_password, email, users)
    if not valid_data[0]:
        conn.close()
        return valid_data
    else:
        salt = uuid4().hex
        hash_password = sha512((password + salt) * 10000).hexdigest()
        q = 'SELECT COUNT(*) FROM teacher_database'
        num_rows = c.execute(q).fetchone()[0]
        q = 'INSERT INTO teacher_database (teacher_id, username, password, salt, first_name, last_name, email, school, room) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        c.execute(q, (num_rows + 1, username, hash_password, salt, first_name, last_name, email, school, room))
        conn.commit()
        conn.close()
        return [True, "Successful Account Creation"]


def get_dates():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "availability_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return []
    q = 'SELECT DISTINCT date FROM availability_database'
    dates = c.execute(q)
    date_list = []
    for date in dates:
        date_list.append(date[0])
    conn.close()
    return date_list


def get_schools():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "teacher_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return []
    q = 'SELECT DISTINCT school FROM teacher_database'
    schools = c.execute(q)
    school_list = []
    for school in schools:
        school_list.append(school[0])
    conn.close()
    return school_list


def get_teachers(school):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "teacher_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return []
    q = 'SELECT last_name, first_name, teacher_id FROM teacher_database WHERE SCHOOL = ?'
    teachers = c.execute(q, (school,))
    conn.close()
    return teachers


# Availablity Database --------------------------------------------------------------------------------------------------------------------------------------
"""
Teacher Availablity Database - Stores when teachers are available
+------------+------+-------+
| Teacher_ID | Date | Times |
+------------+------+-------+
| INT        | TEXT | TEXT  | 
+------------+------+-------+
"""


def set_teacher_availability(TID, date, time):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'CREATE TABLE IF NOT EXISTS availability_database (teacher_id INT, date TEXT, time TEXT)'
    c.execute(q)
    q = 'SELECT teacher_id, date FROM availability_database'
    prev = c.execute(q)
    for entry in prev:
        if (entry[0] == TID and entry[1] == date):
            q = 'DELETE FROM availability_database WHERE TEACHER_ID = ? AND DATE = ?'
            c.execute(q, (TID, date))
    q = 'INSERT INTO availability_database (teacher_id, date, time) VALUES (?, ?, ?)'
    c.execute(q, (TID, date, time))
    conn.commit()
    conn.close()


def get_all_available(date, school):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "availability_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return []
    q = 'SELECT teacher_id FROM availability_database WHERE DATE = ?'
    res = c.execute(q, (date,))
    teach = []
    for entry in res:
        teach.append(entry[0])
    q = 'SELECT teacher_id, first_name, last_name FROM teacher_database WHERE SCHOOL = ?'
    res = c.execute(q, (school,))
    teachers = []
    for entry in res:
        if entry[0] in teach:
            teachers.append(entry)
    return teachers

    

# Appointment Database --------------------------------------------------------------------------------------------------------------------------------------
"""
Parent Teacher Conference Database - Stores the different Appointments
+-----------+------------+------+------+----------------+
| Parent_ID | Teacher_ID | Date | Time | Section Number |
+-----------+------------+------+------+----------------+
| INT       | INT        | TEXT | TEXT | INT            |
+-----------+------------+------+------+----------------+
"""

def make_appointment(PID, TID, date, time, section_num):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'CREATE TABLE IF NOT EXISTS appointment_database (parent_id INT, teacher_id INT, date TEXT, time TEXT, section INT)'
    c.execute(q)
    q = 'SELECT teacher_id, date, time, section FROM appointment_database'
    appointments = c.execute(q)
    for entry in appointments:
        if (entry[0] == TID and entry[1] == date and entry[2] == time and entry[3] == section_num):
            conn.close()
            return [False, TID]
    q = 'INSERT INTO appointment_database (parent_id, teacher_id, date, time, section) VALUES (?, ?, ?, ?, ?)'
    c.execute(q, (PID, TID, date, time, section_num))
    conn.commit()
    conn.close()
    return [True, -1]


def get_teacher_appointments(TID, date):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "appointment_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return []
    q = 'SELECT parent_id, time, section FROM appointment_database WHERE TEACHER_ID = ? AND DATE = ?'
    appointments = c.execute(q, (TID,date))
    list_appoint = []
    for x in appointments:
        print x
        temp = []
        for z in x:
            temp.append(z)
        list_appoint.append(temp)
    for entry in list_appoint:
        PID = entry[0]
        q = 'SELECT first_name, last_name FROM parent_database WHERE PARENT_ID = ?'
        extra = c.execute(q, (PID,)).fetchone()
        print extra
        extra1 = []
        for x in extra:
            extra1.append(x)
        entry.extend(extra1)
    conn.close()
    return list_appoint


def get_parent_appointments(PID, date):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "appointment_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return []
    q = 'SELECT teacher_id, time, section FROM appointment_database WHERE PARENT_ID = ? AND DATE = ?'
    appointments = c.execute(q, (PID,date))
    list_appoint = []
    for x in appointments:
        print x
        temp = []
        for z in x:
            temp.append(z)
        list_appoint.append(temp)
    for entry in list_appoint:
        TID = entry[0]
        q = 'SELECT first_name, last_name FROM teacher_database WHERE TEACHER_ID = ?'
        extra = c.execute(q, (TID,))
        print extra
        extra1 = []
        for x in extra:
            extra1.append(x)
        entry.extend(extra1)
    conn.close()
    return list_appoint

#Miscellaneous------------------------------------

def get_teacher_name(TID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "teacher_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return []
    q = 'SELECT first_name, last_name FROM teacher_database WHERE TEACHER_ID = ?'
    res = c.execute(q, (TID,)).fetchone()
    name = []
    for entry in res:
        name.append(entry)
    conn.close()
    return name
    
def get_time(date):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "availability_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return []
    q = 'SELECT time FROM availability_database WHERE DATE = ?'
    times = c.execute(q, (date,)).fetchone()
    time = []
    for entry in times:
        time.append(entry)
    conn.close()
    return time
    
