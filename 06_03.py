import psycopg2

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
insert_data_sql = "INSERT INTO homework (id, \"last name\", \"year of birth\", \"time of purchase\") VALUES (%s, %s, %s, %s);"

def insert_data_from_file(filename, cursor):
    with open(filename, 'r') as file:
        next(file)  # Skip the column names
        for line in file:
            data = line.strip().split(';')
            cursor.execute(insert_data_sql, data)

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
    insert_data_from_file(data_file, cursor) # inserts data from file into the database
    conn.commit() # permamently saves the changes to database

    retrieve_data() # Retrieves and prints the data

    cursor.close() # Closes the cursor after the program is done
    conn.close() # closes the connection after the program is done

if __name__ == "__main__":
    main()
