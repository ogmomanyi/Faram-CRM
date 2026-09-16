from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Select query executed successfully:', query)
        return rows
    except Error as e:
        logging.error(f'Error executing select query: {e}')
        return None

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    connection = connect_to_mysql()
    if connection:
        query = "SELECT * FROM Suppliers_Contacts"
        rows = execute_select_query(connection, query)
        connection.close()
        if rows:
            return jsonify(rows)
        else:
            return jsonify([])
    else:
        return jsonify([])

@app.route('/api/suppliers', methods=['POST'])
def add_supplier():
    data = request.get_json()
    name = data.get('name')
    contact_person = data.get('contact_person')
    phone = data.get('phone')
    email = data.get('email')
    connection = connect_to_mysql()
    if connection:
        query = """
        INSERT INTO Suppliers_Contacts (Name, Contact_Person, Phone, Email)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        Contact_Person=VALUES(Contact_Person), Phone=VALUES(Phone), Email=VALUES(Email)
        """
        values = (name, contact_person, phone, email)
        execute_query(connection, query, values)
        connection.close()
        return jsonify({"message": "Supplier added/updated successfully"})
    else:
        return jsonify({"message": "Failed to connect to the database"})

@app.route('/api/clients', methods=['GET'])
def get_clients():
    connection = connect_to_mysql()
    if connection:
        query = "SELECT * FROM Client_Contacts"
        rows = execute_select_query(connection, query)
        connection.close()
        if rows:
            return jsonify(rows)
        else:
            return jsonify([])
    else:
        return jsonify([])

@app.route('/api/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    name = data.get('name')
    contact_person = data.get('contact_person')
    phone = data.get('phone')
    email = data.get('email')
    connection = connect_to_mysql()
    if connection:
        query = """
        INSERT INTO Client_Contacts (Name, Contact_Person, Phone, Email)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        Contact_Person=VALUES(Contact_Person), Phone=VALUES(Phone), Email=VALUES(Email)
        """
        values = (name, contact_person, phone, email)
        execute_query(connection, query, values)
        connection.close()
        return jsonify({"message": "Client added/updated successfully"})
    else:
        return jsonify({"message": "Failed to connect to the database"})

@app.route('/api/leads', methods=['GET'])
def get_leads():
    connection = connect_to_mysql()
    if connection:
        query = "SELECT * FROM Leads"
        rows = execute_select_query(connection, query)
        connection.close()
        if rows:
            return jsonify(rows)
        else:
            return jsonify([])
    else:
        return jsonify([])

@app.route('/api/leads', methods=['POST'])
def add_lead():
    data = request.get_json()
    date_created = data.get('date_created')
    lead_status = data.get('lead_status')
    client_name = data.get('client_name')
    product = data.get('product')
    value = data.get('value')
    supplier_name = data.get('supplier_name')
    lead_owner = data.get('lead_owner')
    lead_source = data.get('lead_source')
    notes = data.get('notes')
    connection = connect_to_mysql()
    if connection:
        query = """
        INSERT INTO Leads (Date_Created, Lead_Status, Client_Name, Product, Value, Supplier_Name, Lead_Owner, Lead_Source, Notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        Lead_Status=VALUES(Lead_Status), Client_Name=VALUES(Client_Name), Product=VALUES(Product), Value=VALUES(Value), Supplier_Name=VALUES(Supplier_Name), Lead_Owner=VALUES(Lead_Owner), Lead_Source=VALUES(Lead_Source), Notes=VALUES(Notes)
        """
        values = (date_created, lead_status, client_name, product, value, supplier_name, lead_owner, lead_source, notes)
        execute_query(connection, query, values)
        connection.close()
        return jsonify({"message": "Lead added/updated successfully"})
    else:
        return jsonify({"message": "Failed to connect to the database"})

@app.route('/api/products', methods=['GET'])
def get_products():
    connection = connect_to_mysql()
    if connection:
        query = "SELECT * FROM Products"
        rows = execute_select_query(connection, query)
        connection.close()
        if rows:
            return jsonify(rows)
        else:
            return jsonify([])
    else:
        return jsonify([])

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = data.get('product')
    supplier = data.get('supplier')
    contact_person = data.get('contact_person')
    phone = data.get('phone')
    email = data.get('email')
    connection = connect_to_mysql()
    if connection:
        query = """
        INSERT INTO Products (Product, Supplier, Contact_Person, Phone, Email)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        Supplier=VALUES(Supplier), Contact_Person=VALUES(Contact_Person), Phone=VALUES(Phone), Email=VALUES(Email)
        """
        values = (product, supplier, contact_person, phone, email)
        execute_query(connection, query, values)
        connection.close()
        return jsonify({"message": "Product added/updated successfully"})
    else:
        return jsonify({"message": "Failed to connect to the database"})

if __name__ == "__main__":
    app.run(debug=True)
