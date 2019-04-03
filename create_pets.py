""" Creates the DB Schema for the pets database """
import sqlite3
from sqlite3 import OperationalError

def create_connection(db_file):
    """ Creates connection to SQLite db """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except OperationalError as connection_error:
        print connection_error
    return None

def reset_db(conn, tables):
    """ Reset function - drops all tables from the DB """
    for table in tables:
        try:
            cur = conn.cursor()
            cur.execute('DROP TABLE IF EXISTS {}'.format(table))
        except OperationalError as execute_error:
            print execute_error
    return cur.lastrowid


def create_table(conn, sql_string):
    """ Create a new table from the passed sql string """
    try:
        sql_cursor = conn.cursor()
        sql_cursor.execute(sql_string)
    except OperationalError as execution_error:
        print execution_error

def main():
    """ Builds out the Pet database
    Drops all tables first, then rebuilds them"""
    dbtables = ['person', 'pet', 'person_pet']

    person_table = """
    CREATE TABLE IF NOT EXISTS person
  ( 
     id         INTEGER PRIMARY KEY, 
     first_name TEXT, 
     last_name  TEXT, 
     age        INTEGER 
  ); 
    """

    pet_table = """
    CREATE TABLE IF NOT EXISTS pet
  ( 
     id    INTEGER PRIMARY KEY, 
     name  TEXT, 
     breed TEXT, 
     age   INTEGER, 
     dead  INTEGER 
  ); 
    """

    person_pet_table = """
    CREATE TABLE IF NOT EXISTS person_pet
  ( 
     person_id INTEGER, 
     pet_id    INTEGER 
  ); 
    """

    db_connection = create_connection('pets.db')
    if db_connection:
        reset_db(db_connection, dbtables)
        create_table(db_connection, person_table)
        create_table(db_connection, pet_table)
        create_table(db_connection, person_pet_table)

if __name__ == "__main__":
    main()
