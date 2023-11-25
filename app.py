import mysql.connector
from mysql.connector import Error  # error function separately
import pandas as pd

# function to connect to MySQL server


def create_server_connection(host_name, user_name, user_password):
    connection = None  # close any existing connection
    try:  # try ... exept - handle any error and don't crush program
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print('MySQL Database connection')
    except Error as err:
        print(f'Error: "{err}"')

    return connection


connection = create_server_connection('localhost', 'root', '')
