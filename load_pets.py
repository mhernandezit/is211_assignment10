""" A module to populate a DB with values """
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

def create_person(conn, person):
    """ Inserts person tuples into person table """
    sql = ''' INSERT INTO person
            ( 
                        id, 
                        first_name, 
                        last_name, 
                        age 
            ) 
            VALUES(?, ?, ?, ?)
    '''
    try:
        cur = conn.cursor()
        cur.execute(sql, person)
    except Error as execute_error:
        print execute_error
    return cur.lastrowid

def create_pet(conn, pet):
    """ Inserts pet tuples into pet table """
    sql = ''' INSERT INTO pet
            ( 
                        id, 
                        NAME, 
                        breed, 
                        age, 
                        dead 
            ) 
            VALUES(?, ?, ?, ?, ?)
    '''
    try:
        cur = conn.cursor()
        cur.execute(sql, pet)
    except Error as execute_error:
        print execute_error
    return cur.lastrowid

def create_person_pet(conn, person_pet):
    """ Inserts pet, person tuple into person_pet table """
    sql = ''' INSERT INTO person_pet
            ( 
                        person_id, 
                        pet_id 
            ) 
            VALUES(?, ?)
    '''
    try:
        cur = conn.cursor()
        cur.execute(sql, person_pet)
    except Error as execute_error:
        print execute_error
    return cur.lastrowid

def main():
    """ Main function builds the tuples we will be
    loading into the database load scripts """
    database = 'pets.db'
    person_data = [(1, 'James', 'Smith', 41),
                   (2, 'Diana', 'Greene', 23),
                   (3, 'Sara', 'White', 27),
                   (4, 'William', 'Gibson', 23)]
    pet_data = [(1, 'Rusty', 'Dalmation', 4, 1),
                (2, 'Bella', 'AlaskanMalamute', 3, 0),
                (3, 'Max', 'CockerSpaniel', 1, 0),
                (4, 'Rocky', 'Beagle', 7, 0),
                (5, 'Rufus', 'CockerSpaniel', 1, 0),
                (6, 'Spot', 'Bloodhound', 2, 1)]
    person_pet_data = [(1, 1),
                       (1, 2),
                       (2, 3),
                       (2, 4),
                       (3, 5),
                       (4, 6)]
    conn = create_connection(database)
    with conn:
        for person in person_data:
            create_person(conn, person)
        for pet in pet_data:
            create_pet(conn, pet)
        for person_pet in person_pet_data:
            create_person_pet(conn, person_pet)

if __name__ == "__main__":
    main()
