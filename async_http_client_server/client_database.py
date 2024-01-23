import MySQLdb
import json

def db_connect():
    """
    returns db object
    """
    return MySQLdb.connect(
        host = "localhost",
        user = "root",
        password = "vidoosh123",
        db = "client_data"
    )

def insert_data(cursor, client_id, data):
    """
    insert data into the db
    """
    data = json.dumps(data)
    cursor.execute("INSERT INTO client_details (client_id, data) VALUES (%s, %s)", (client_id, data))
    

def data_lookup(cursor, client_id):
    """
    returns the client data if the client_id is present
    """
    cursor.execute("SELECT data from client_details WHERE client_id = %s", (client_id,))
    result = cursor.fetchall()

    return result


