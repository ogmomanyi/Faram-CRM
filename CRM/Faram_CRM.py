import mysql.connector
from mysql.connector import Error
import logging
import os

logging.basicConfig(filename='crm_errors.log', level=logging.ERROR)

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='EduMomz13-.',
            database='Faram_CRM'
        )
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        logging.error(f'Error connecting to MySQL: {e}')
        return None

def execute_query(connection, query, values=None):
    try:
        cursor = connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print('Query executed successfully:', query)
    except Error as e:
        logging.error(f'Error executing query: {e}')

def execute_select_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Select query executed successfully:', query)
        return rows
    except Error as e:
        logging.error(f'Error executing select query: {e}')
        return None

# Main script
if __name__ == "__main__":
    connection = connect_to_mysql()
    if connection:
        try:
            # Example select query
            query = "SELECT * FROM Suppliers_Contacts"
            rows = execute_select_query(connection, query)
            if rows:
                for row in rows:
                    print(row)
            else:
                print('No rows returned from the select query')
            
            # Example insert query with ON DUPLICATE KEY UPDATE
            query = """
            INSERT INTO Suppliers_Contacts (Name, Contact_Person, Phone, Email)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            Contact_Person=VALUES(Contact_Person), Phone=VALUES(Phone), Email=VALUES(Email)
            """
            values = ('TestSupplier', 'John Doe', '1234567890', 'john@example.com')
            execute_query(connection, query, values)
        
        except Error as e:
            logging.error(f"An error occurred: {e}")
        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")
