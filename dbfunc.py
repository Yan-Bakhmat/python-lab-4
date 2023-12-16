import mysql.connector
from mysql.connector import Error  # error function separately

# function to connect to MySQL server


def create_server_connection(host_name, user_name, user_password):
    connection = None  # close any existing connection
    try:  # try ... exept - handle any error and don't crush program
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print('MySQL Database connection successful')
    except Error as err:
        print(f'Error: "{err}"')
    return connection

# function to connect to database


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            datebase=db_name
        )
        print('MySQL Database connection successful')
    except Error as err:
        print(f"Error '{err}'")
    return connection

# function to create database


def create_datebase(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Datebase created seccessfully")
    except Error as err:
        print(f'Error "{err}"')
