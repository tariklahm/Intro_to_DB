import mysql.connector

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",  # your MySQL server host
        user="root",       # your MySQL username
        password=""        # your MySQL password
    )

    cursor = connection.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as error:
    print("Failed to connect to MySQL:", error)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()