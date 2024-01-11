import psycopg2
import json

# Load database info
data = json.load(open("key_config.json"))
database_name = data['DATABASE']['database_name']
user = data['DATABASE']['username']
password = data['DATABASE']['password']
host = "localhost"

def connect_to_db():
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
        return conn, cursor

    except Exception as e:
        print(f"Error: {e}")


def close_db_connection(conn, cursor):
    cursor.close()
    conn.close()


# Function to execute SQL queries from a file
def execute_query_from_file(query_file_path, get=False, insert=False, data=None):
    conn, cursor = connect_to_db()

    try:
        # Execute the query from the file
        with open(query_file_path, 'r') as file:
            query = file.read()

        if insert:
            for index, row in data.iterrows():
                # Execute the insertion query for the current row
                cursor.execute(query, dict(row))
        else:
            cursor.execute(query)

        # Fetch the result
        result = cursor.fetchall()

        # Commit the changes (if any)
        conn.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        close_db_connection(conn, cursor)
        if get:
            return result

