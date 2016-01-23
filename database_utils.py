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
        return False
    q = 'SELECT password, salt FROM parent_database WHERE username = ?'
    pepper_and_salt = c.execute(q, (username,)).fetchone()
    if pepper_and_salt and sha512((password + pepper_and_salt[1]) * 10000).hexdigest() == pepper_and_salt[0]:
        q = "SELECT parent_id FROM parent_database WHERE username = ?"
        id = c.execute(q, (username,)).fetchone()
        conn.close()
        return id
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
        return False
    q = 'SELECT password, salt FROM teacher_database WHERE username = ?'
    pepper_and_salt = c.execute(q, (username,)).fetchone()
    conn.close()
    if not pepper_and_salt or sha512((password + pepper_and_salt[1]) * 10000).hexdigest() != pepper_and_salt[0]:
        return False
    return True


def valid_create_teacher(username, password, repeat_password, first_name, last_name, email, school, room):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'CREATE TABLE IF NOT EXISTS teacher_database (teacher_id INT, username TEXT, password INT, salt INT, first_name TEXT, last_name TEXT, email TEXT, school TEXT, room TEXT)'
    c.execute(q)
    q = 'SELECT username, email FROM teacher_database'
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
    conn.close()
    return schools


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
+------------+------+-------+----------+
| Teacher_ID | Date | Times | Sections |
+------------+------+-------+----------+
| INT        |      |       | INT      |
+------------+------+-------+----------+
"""


# Appointment Database --------------------------------------------------------------------------------------------------------------------------------------
"""
Parent Teacher Conference Database - Stores the different Appointments
+-----------+------------+------+------+----------------+
| Parent_ID | Teacher_ID | Date | Time | Section Number |
+-----------+------------+------+------+----------------+
| INT       | INT        |      |      | INT            |
+-----------+------------+------+------+----------------+
"""

def get_teacher_appointments(TID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "appointment_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return []
    q = 'SELECT parent_id, date, time, section_number FROM appointment_database WHERE TEACHER_ID = ?'
    appointments = c.execute(q, (TID,))
    for entry in appointments:
        PID = entry[0]
        q = 'SELECT first_name, last_name FROM parent_database WHERE PARENT_ID = ?'
        name = c.execute(q, (PID,))
        entry.extend(name)
    conn.close()
    return appointments

def get_parent_appointments(PID):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "appointment_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return []
    q = 'SELECT teacher_id, date, time FROM appointment_database WHERE PARENT_ID = ?'
    appointments = c.execute(q, (PID,))
    for entry in appointments:
        TID = entry[0]
        q = 'SELECT first_name, last_name FROM teacher_database WHERE TEACHER_ID = ?'
        name = c.execute(q, (TID,))
        entry.extend(name)
    conn.close()
    return appointments
