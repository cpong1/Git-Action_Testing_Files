import mysql.connector

try:
    # Replace with your database connection details
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="test",
        password=""
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")

        data = cursor.fetchone()
        print(f"Connected to MySQL database (Server version: {data[0]})")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
