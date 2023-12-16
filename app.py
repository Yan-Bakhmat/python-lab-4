import pandas as pd
from dbfunc import *

password = input('Please enter your server password: ')
# the third parameter should be the password from your server
connection = create_server_connection('localhost', 'root', password)
create_datebase_query = "CREATE DATABASE dut"
create_datebase(connection, create_datebase_query)
