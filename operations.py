import sqlite3
import pandas as pd
import database_functions

# Connect to SQLite database
conn = sqlite3.connect('master_database.db')
cursor = conn.cursor()


database_functions.create_new_user("ray", "chihdia@gmail.com","dnqjnleqndl2")


