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
# Returns a Boolean
# True if successful, False if unsuccessful
def valid_parent_login(username, password):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'SELECT name FROM sqlite_master WHERE TYPE = "table" AND NAME = "parent_database"'
    c.execute(q)
    if not c.fetchone():
        conn.close()
        return False
    q = 'SELECT password, salt FROM parent_database WHERE username = ?'
    pepper_and_salt = c.execute(q, (username)).fetchone()
    conn.close()
    if not pepper_and_salt or sha512((password + pepper_and_salt[1]) * 10000).hexdigest() != pepper_and_salt[0]:
        return False
    return True


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
+------------+----------+----------+------+------------+-----------+-------+--------+------------+------+
| Teacher_ID | Username | Password | Salt | First Name | Last Name | Email | School | Department | Room |
+------------+----------+----------+------+------------+-----------+-------+--------+------------+------+
| INT        | TEXT     | INT      | INT  | TEXT       | TEXT      | TEXT  | TEXT   | TEXT       | TEXT |
+------------+----------+----------+------+------------+-----------+-------+--------+------------+------+
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
    pepper_and_salt = c.execute(q, (username)).fetchone()
    conn.close()
    if not pepper_and_salt or sha512((password + pepper_and_salt[1]) * 10000).hexdigest() != pepper_and_salt[0]:
        return False
    return True


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
+------------+----------+----------+------+------------+-----------+-------+--------+------------+------+
| Teacher_ID | Username | Password | Salt | First Name | Last Name | Email | School | Department | Room |
+------------+----------+----------+------+------------+-----------+-------+--------+------------+------+
| INT        | TEXT     | INT      | INT  | TEXT       | TEXT      | TEXT  | TEXT   | TEXT       | TEXT |
+------------+----------+----------+------+------------+-----------+-------+--------+------------+------+
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
    pepper_and_salt = c.execute(q, (username)).fetchone()
    conn.close()
    if not pepper_and_salt or sha512((password + pepper_and_salt[1]) * 10000).hexdigest() != pepper_and_salt[0]:
        return False
    return True


def valid_create_teacher(username, password, repeat_password, first_name, last_name, email, school, department, room):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = 'CREATE TABLE IF NOT EXISTS teacher_database (teacher_id INT, username TEXT, password INT, salt INT, first_name TEXT, last_name TEXT, email TEXT, school TEXT, department TEXT, room TEXT)'
    c.execute(q)
    q = 'SELECT username, email FROM teacher_database'
    valid_data = utils.valid_data(username, password, repeat_password, email, users)
    if not valid_data[0]:
        conn.close()
        return valid_data
    else:
        salt = uuid4().hex
        hash_password = sha512((password + salt) * 10000).hexdigest()
        q = 'SELECT COUNT(*) FROM parent_database'
        num_rows = c.execute(q).fetchone()[0]
        q = 'INSERT INTO parent_database (teacher_id, username, password, salt, first_name, last_name, email, school, department, room) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        c.execute(q, (num_rows + 1, username, hash_password, salt, first_name, last_name, email, school, Department, room))
        conn.commit()
        conn.close()
        return [True, "Successful Account Creation"]
    return False
