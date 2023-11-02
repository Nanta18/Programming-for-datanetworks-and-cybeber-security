# Always the same but names are random

import random
import psycopg2
from datetime import datetime, timedelta

# All the details needed to acces the database
db_details = {
    'dbname': 'homework',
    'user': 'dncs-db',
    'password': 'dbSikrit11',
    'host': 'localhost',
}

# If the table already exists drops it
drop_homework_table = "DROP TABLE IF EXISTS homework;"

# Creates the table
create_homework_table = """
CREATE TABLE homework (
    id SERIAL PRIMARY KEY,
    "last name" VARCHAR(255),
    "year of birth" INTEGER,
    "time of purchase" TIMESTAMP
);
"""
# SQL query to insert values into the table in a SQL injection safe way
insert_data_sql = "INSERT INTO homework (\"last name\", \"year of birth\", \"time of purchase\") VALUES (%s, %s, %s)"


def generate_random_name(number):
    name = ""
    for _ in range(5):
        random_number_for_name = number.randint(1, 26)
        if 1 <= random_number_for_name <= 26:
            name += chr(ord('A') + random_number_for_name - 1)
    return name

def generate_random_date(seed):
    random.seed(seed)

    start_date = datetime(2020, 1, 1)
    end_date = datetime(2022, 12, 31)

    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    # Generate random hours, minutes, and seconds
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    random_seconds = random.randint(0, 59)
    
    random_date = random_date.replace(hour=random_hours, minute=random_minutes, second=random_seconds)
    
    return random_date


def insert_random_data(cursor):
    for x in range(10000):
        persistent_randomn_num_gen = random.Random(x)
        random_number = persistent_randomn_num_gen.randint(1, 200000)

        random_year = persistent_randomn_num_gen.randint(1945, 2023)
        random_name = generate_random_name(persistent_randomn_num_gen)
        random_date = generate_random_date(random_number)

        cursor.execute(insert_data_sql, (random_name, random_year, random_date))

def retrieve_data():
    # Connect to the database and create a cursor
    conn = psycopg2.connect(**db_details)
    cursor = conn.cursor()

    # SQL query to select everything
    select_query = 'SELECT * FROM homework;'
    cursor.execute(select_query)

    # Creates a variable for all the data to be stored in
    results = cursor.fetchall()

    # prints the data row by row
    for row in results:
        print(row)

    # Closes the cursor and the database
    cursor.close()
    conn.close()


def main():
    
    conn = psycopg2.connect(**db_details) # Connects to the database
    cursor = conn.cursor() # Opens a cursor to access and modify the database

    cursor.execute(drop_homework_table) # Drops the homework table

    cursor.execute(create_homework_table) # Creates the homework table

    conn.commit() # permamently saves the changes to database

    data_file = "data.txt" # Defines where the data will be taken
    insert_random_data(cursor) # inserts data from file into the database
    conn.commit() # permamently saves the changes to database

    retrieve_data() # Retrieves and prints the data

    cursor.close() # Closes the cursor after the program is done
    conn.close() # closes the connection after the program is done

if __name__ == "__main__":
    main()
