import mysql.connector
from flask import current_app

def get_db_connection():
    config = current_app.config['DB_CONFIG']
    conn = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )
    return conn