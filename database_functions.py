import sqlite3
import pandas as pd


# add new user to the userinfo table, create user_data table
def create_new_user(user_name, email, password):
    conn = sqlite3.connect("master_database.db")
    cursor = conn.cursor()
    # the userinfo_table
    cursor.execute('''CREATE TABLE IF NOT EXISTS userinfo_table (
                            id INTEGER PRIMARY KEY,
                            user_name TEXT,
                            email TEXT,
                            password
                         )''')

    cursor.execute('''INSERT INTO userinfo_table (user_name, email, password) VALUES (?, ?, ?)''',
                   (user_name, email, password))
    conn.commit()

    user_table_name = email.replace("@", "").replace(".com", "")
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {user_table_name}(
                            date_time DATETIME PRIMARY KEY,
                            list_progress TEXT
                         )''')
    conn.commit()
    cursor.close()
    conn.close()


def add_training_data(email, date_time, list_progress):
    conn = sqlite3.connect("master_database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO {email}  (date_time, list_progress) VALUES (?, ?,?)".format(email=email)
                   , (date_time, list_progress))
    conn.commit()
    cursor.close()
    conn.close()
