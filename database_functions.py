import sqlite3
import pandas as pd

# Connect to SQLite database

def create_new_user(user_name, email, password):
    conn = sqlite3.connect("master_database.db")
    cursor = conn.cursor()
    # the userinfo_table
    cursor.execute('''CREATE TABLE IF NOT EXISTS userinfo_table (
                            id INTEGER PRIMARY KEY,
                            user_name TEXT,
                            email TEXT,  
                            password TEXT
                         )''')

    cursor.execute('''INSERT INTO userinfo_table (user_name, email, password) VALUES (?, ?, ?)''',
                   (user_name, email, password))

    # initialize user data table, for now assume email is a primary key
    cursor.execute('''CREATE TABLE IF NOT EXISTS {email} (
                            date_time DATETIME PRIMARY KEY,
                            list_progress TEXT
                         )'''.format(email=email))
    conn.commit()
    cursor.close()
    conn.close()


def add_training_data(email, date_time, list_progress):
    conn = sqlite3.connect("master_database")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO {email}  (date_time, list_progress) VALUES (?, ?,?)".format(email=email)
                   , (date_time, list_progress))
