from sqlite3 import connect
from sqlite3.dbapi2 import Cursor

DB_NAME = "database/user_records.db"  # database name


# create database inside database folder if not exists
connection = connect(DB_NAME)

cursor = connection.cursor()


def create_table():
    """function to create table inside database"""
    # create table user inside database if not exists
    table_script = '''CREATE TABLE IF NOT EXISTS User(
                    full_name VARCHAR(255),
                    country VARCHAR(150)
                );
                '''
    cursor.executescript(table_script)
    connection.commit()


def insert_record(fullname, country):
    """function to insert record inside table"""
    cursor.execute("INSERT INTO User(full_name, country) VALUES(?, ?)",
                   (fullname, country))
    connection.commit()


def fetch_records():
    """function to fetch User records"""
    data = cursor.execute("SELECT * FROM User")
    return data
