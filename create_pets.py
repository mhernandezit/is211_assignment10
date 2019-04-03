""" Creates the DB Schema for the pets database """
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Creates connection to SQLite db """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as connection_error:
        print connection_error
    return None

def create_table(conn, sql_string):
    """ Create a new table from the passed sql string """
    try:
        sql_cursor = conn.cursor()
        sql_cursor.execute(sql_string)
    except Error as execution_error:
        print execution_error

if __name__ == "__main__":
    PERSON_TABLE = """
    CREATE TABLE IF NOT EXISTS person
  ( 
     id         INTEGER PRIMARY KEY, 
     first_name TEXT, 
     last_name  TEXT, 
     age        INTEGER 
  ); 
    """

    PET_TABLE = """
    CREATE TABLE IF NOT EXISTS pet
  ( 
     id    INTEGER PRIMARY KEY, 
     name  TEXT, 
     breed TEXT, 
     age   INTEGER, 
     dead  INTEGER 
  ); 
    """

    PERSON_PET_TABLE = """
    CREATE TABLE IF NOT EXISTS person_pet
  ( 
     person_id INTEGER, 
     pet_id    INTEGER 
  ); 
    """

    DB_CONNECTION = create_connection('pets.db')
    if DB_CONNECTION:
        create_table(DB_CONNECTION, PERSON_TABLE)
        create_table(DB_CONNECTION, PET_TABLE)
        create_table(DB_CONNECTION, PERSON_PET_TABLE)
