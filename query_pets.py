""" A module to query a DB  """
import sqlite3
from sqlite3 import Error
from sqlite3 import OperationalError

def create_connection(db_file):
    """ Creates connection to SQLite db """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as connection_error:
        print connection_error
    return None

def query_user_id(conn):
    """ User input function - asks a user for an ID then
    forwards that ID to a select_person_by_id function"""
    user_id = 0
    while (user_id != -1) is True:
        user_input = raw_input('Please enter a person ID: ')
        try:
            user_id = int(user_input)
            #select_person_by_id(conn, user_id)
            select_pets_by_person(conn, user_id)
        except ValueError:
            print "Please enter an integer"

def select_pets_by_person(conn, person_id):
    """ SQL query to pull the pets that are associated with a
    person ID """
    sql = """
    SELECT person.first_name 
       || ' ' 
       || person.last_name AS `Owner`, 
       pet.name            AS `Pet Name`, 
       pet.breed           AS `Pet Breed`, 
       pet.age             AS `Pet Age` 
    FROM   person_pet 
       INNER JOIN person 
               ON person.id = person_pet.person_id 
       INNER JOIN pet 
               ON pet.id = person_pet.pet_id 
    WHERE  person.id = ? 
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, (person_id,))
    except OperationalError, msg:
        print 'SQL error {} while running our code'.format(msg)
    print sql_pp(cur)

def select_person_by_id(conn, person_id):
    """ Function to run a select statement, then print the results
    using our pretty printing function sql_pp """
    sql = '''SELECT * FROM person WHERE id=?'''
    cur = conn.cursor()
    try:
        cur.execute(sql, (person_id,))
    except OperationalError, msg:
        print 'SQL error {} while running our code'.format(msg)
    print sql_pp(cur)

def sql_pp(cursor):
    """ SQL Pretty printer - function to pull results from SQL cli
    and print out the results. Credit for this function goes to
    Steve Holden at
    https://www.oreilly.com/library/view/python-cookbook/0596001673/ch08s11.html
    I edited it to make it more "Pythonic" and to fit my needs here
    Returns a string with the SQL query results
    """
    headers = cursor.description
    data = cursor.fetchall()
    names = []
    lengths = []
    dividers = []

    if not data:
        return "Query Error - PersonID does not exist in Database, please try again"

    # Build out our header row, and our column length list
    for header in headers:
        length = len(header[0])
        if not length:
            length = 12
        length = max(length, len(header[0]))
        names.append(header[0])
        lengths.append(length)

    # Check to see if any column data is too wide, adjust length if it is
    for counter, length in enumerate(lengths):
        for row in data:
            if row[counter]:
                row_length = len(str(row[counter]))
                lengths[counter] = max(row_length, length)
        # Build out the dividers
        dividers.append("-"*lengths[counter])

    # Builds a string output with correct spacing per our length list
    output = " ".join(["%%-%ss" % _ for _ in lengths])

    # Header, divider row string building
    result = [output % tuple(names)]
    result.append(output % tuple(dividers))

    # Build out the data rows
    for row in data:
        result.append(output % row)

    # Return our result string
    return "\n".join(result)


def main():
    """ Main method to create our db connection then run the query """
    pets = create_connection('pets.db')
    query_user_id(pets)

if __name__ == "__main__":
    main()
