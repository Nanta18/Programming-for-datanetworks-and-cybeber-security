import flask
import psycopg2
from flask import request, jsonify

app = flask.Flask(__name__)

#Hardcoded Login details
db_details = {
    'dbname': 'bookstore',  
    'user': 'dncs-db',
    'password': 'dbSikrit11',
    'host': 'localhost',
}

#DATABASE

#Doing database things
def database_function():
    # All the details needed to access the database
    # Update the 'dbname' in db_details
 

    # Connects to the database
    conn = psycopg2.connect(**db_details)
    # Opens a cursor to access and modify the database
    cursor = conn.cursor()

    # Creates the table
    create_homework_table = """
    CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        author VARCHAR(100) NOT NULL,
        year_of_publication INTEGER NOT NULL
    );
    """

    cursor.execute(create_homework_table)  # Execute the SQL statement
    conn.commit()  # Permanently saves the changes to the database

    cursor.close()  # Closes the cursor after the program is done
    conn.close()  # Closes the connection after the program is done

#API

#Creates a site /sell on the webserver which allows a separate POST program to add new books to the SQL database
@app.route('/sell/', methods=['POST'])
def sell_api():

    data = request.get_json()
    
    # Connect to database
    conn = psycopg2.connect(**db_details)
    cursor = conn.cursor()

    add_new_book_to_database = """
    INSERT INTO books (title, author, year_of_publication) VALUES (%s, %s, %s) RETURNING id;
    """
    cursor.execute(add_new_book_to_database, (data['title'], data['author'], data['year_of_publication']))
    book_id = cursor.fetchone()[0]

    conn.commit()  # Permanently saves the changes to the database
    cursor.close()  # Closes the cursor after the program is done
    conn.close()  # Closes the connection after the program is done

    return jsonify({"message": "Yeah, we got your book", "book_id": book_id})

#Creates a site /list on the webserver which returns the list of titles in the database
@app.route('/list/', methods=['GET'])
def list_api():    
    # Connects to the database
    conn = psycopg2.connect(**db_details)
    # Opens a cursor to access the database
    cursor = conn.cursor()

    # Execute the SQL query to select titles from the books table
    cursor.execute("SELECT title FROM books")
    titles = [row[0] for row in cursor.fetchall()]

    cursor.close()  # Closes the cursor after the program is done
    conn.close()  # Closes the connection after the program is done

    # Prints the titles in console
    for title in titles:
        print(title)

    # Return the list as JSON
    return jsonify({"titles": titles})

@app.route('/purchase/<int:item_id>', methods=['GET'])
def purchase_api(item_id):
    # Connects to the database
    conn = psycopg2.connect(**db_details)
    # Opens a cursor to access the database
    cursor = conn.cursor()

    delete_a_book_from_database = """
    DELETE FROM books WHERE id = %s;
"""

    cursor.execute(delete_a_book_from_database, (item_id,))

    conn.commit()  # Permanently saves the changes to the database
    cursor.close()  # Closes the cursor after the program is done
    conn.close()  # Closes the connection after the program is done

    return jsonify({"message": "ok"})

#Run app and call the functions
database_function()
app.run()