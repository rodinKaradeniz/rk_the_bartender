import psycopg2
import json


# Load database info
data = json.load(open("key_config.json"))
database_name = data['DATABASE']['database_name']
user = data['DATABASE']['username']
password = data['DATABASE']['password']
host = "localhost"


# Function to execute SQL queries from a file
def execute_query_from_file(query_file_path):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=database_name,
            user=user,
            password=password,
            host=host
        )

        # Create a cursor to interact with the database
        cursor = conn.cursor()

        # Execute the query from the file
        with open(query_file_path, 'r') as file:
            query = file.read()
            cursor.execute(query)

        # Fetch and print the result (if applicable)
        result = cursor.fetchall()
        print(result)

        # Commit the changes (if any)
        conn.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
