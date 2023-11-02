import random
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
    "time of purchase" INTEGER
);
"""
# SQL query to insert values into the table in a SQL injection safe way
insert_data_sql = "INSERT INTO homework (\"last name\", \"year of birth\", \"time of purchase\") VALUES (%s, %s, %s)"


def generate_random_name():
    return random.choice(last_names)

# List of over 300 random names
last_names = [
    "Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Harris", "Jackson",
    "Martinez", "Gonzalez", "Lopez", "Perez", "Sanchez", "Ramirez", "Torres", "Nguyen", "Adams", "Mitchell",
    "Carter", "James", "Roberts", "Turner", "Phillips", "Martin", "Thompson", "Evans", "Scott", "Cooper",
    "Anderson", "Hernandez", "King", "Green", "Lee", "Hall", "Young", "Hill", "Nelson", "Baker",
    "Garcia", "Rodriguez", "Parker", "White", "Lewis", "Wright", "Walker", "Hall", "Morris", "Alexander",
    "King", "Allen", "Bennett", "Rogers", "Morgan", "Ward", "Murphy", "O'Connor", "Harrison", "Sullivan",
    "Cunningham", "Bradley", "Lane", "Dixon", "Black", "Lloyd", "Fox", "Dean", "McCarthy", "George",
    "Mitchelson", "Thompson", "Evanson", "Anderson", "Walters", "Edwards", "Stewart", "Carter", "Phillips",
    "Russell", "Reyes", "Griffin", "Gibson", "Spencer", "Porter", "Murphy", "Dixon", "Wallace", "Wood",
    "Martin", "Shaw", "Wagner", "Warren", "Coleman", "Holmes", "Ferguson", "McDaniel", "Thompson", "Pearson",
    "Hunter", "Brewer", "Fleming", "Watkins", "Powell", "Bryant", "Sims", "Carr", "Owens", "Greer",
    "Vargas", "Gonzales", "Riley", "Howell", "May", "Nunez", "Valdez", "Reeves", "Santiago", "Steele",
    "Brewer", "Salazar", "Shelton", "Chavez", "Payne", "Stevens", "Fitzgerald", "McCoy", "Olson", "Schmidt",
    "Ortega", "Meyers", "Adkins", "Ford", "Quinn", "Rose", "Ramos", "Wade", "Fox", "Barnes",
    "Webster", "Dean", "Carpenter", "Hunt", "Blackwell", "Carlson", "Wall", "Whitney", "Estrada", "Drake",
    "Rowe", "Molina", "Hogan", "Brown", "Keller", "Delgado", "Crawford", "Freeman", "Wells", "Little",
    "Vasquez", "Jacobs", "Reid", "Hoffman", "Brady", "McBride", "Patterson", "Greene", "Carrillo", "Dunn",
    "Banks", "Wilkerson", "Williamson", "Carlson", "Kramer", "Lowe", "Fleming", "Haynes", "Ramos", "Cox",
    "Hicks", "Roberson", "Baldwin", "Barton", "Cruz", "Hawkins", "Lloyd", "Baldwin", "Stevenson", "Kim",
    "Bell", "Bennett", "Morrison", "Boyd", "Lucas", "Waters", "Holt", "Franklin", "Martin", "Ward",
    "Berry", "Grant", "Sparks", "Watson", "Glover", "George", "Carroll", "Mann", "Bryant", "Estrada",
    "Gomez", "Mendez", "Horton", "Bass", "Cole", "Clark", "Garcia", "Foster", "Gray", "Byrd",
    "Pierce", "Ruiz", "Carpenter", "Nichols", "Watson", "Elliott", "Munoz", "Holland", "Fleming", "Blair",
    "Carrillo", "Rice", "Berry", "Garza", "Reeves", "Howard", "Riley", "Ellis", "Fitzgerald", "McDaniel",
    "Gill", "Ramirez", "Day", "Holland", "Brown", "Sanchez", "Gonzales", "Ramos", "Schmidt", "Ward",
    "Porter", "Estrada", "Bell", "King", "Gonzalez", "Green", "Cole", "Keller", "Bryant", "Banks",
    "Mitchell", "George", "Reid", "Walters", "Payne", "Lopez", "Glover", "Hawkins", "Barnes", "Dixon",
    "Boyd", "Roberson", "Murphy", "Jacobs", "Adkins", "Fleming", "Stewart", "Barton", "Franklin", "Greer",
    "Kramer", "Blackwell", "Walters", "Stevenson", "Lloyd", "Elliott", "Gill", "Rowe", "Hicks", "Horton",
    "Drake", "Carr", "Foster", "Fitzgerald", "Pierce", "Gomez", "Gray", "Mann", "Cruz", "Webster",
    "Carroll", "Munoz", "Morrison", "Nichols", "Howard", "Watson", "Berry", "Bass", "Holt", "Lucas",
    "Sparks", "Mendez", "Byrd", "Garcia", "Bell", "Watson", "Ruiz", "Gomez", "Boyd", "Lopez",
    "Mann", "Gonzalez", "King", "Lucas", "Morrison", "Barton", "Holland", "Walters", "George", "Howard",
    "Franklin", "Blair", "Grant", "Green", "Stewart", "Day", "Estrada", "Bell", "Hawkins", "Watson",
    "Carrillo", "Hicks", "Fleming", "Nichols", "Ramirez", "Barnes", "Pierce", "Cole", "Gill", "Fitzgerald",
    "Bryant", "McDaniel", "Munoz", "Martin", "Cox", "Rowe", "Gomez", "Waters", "Clark", "Horton",
    "Schmidt", "Sparks", "Blackwell", "Roberson"
]



def insert_random_data(cursor):
    for x in range(10000):
        persistent_randomn_num_gen = random.Random(x)
        random_number = persistent_randomn_num_gen.randint(1, 200000)

        number_variations1 = random_number * 45
        number_variations2 = random_number - 45
        random_name = generate_random_name() # Returns random name

        cursor.execute(insert_data_sql, (random_name, number_variations1, number_variations2))

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
