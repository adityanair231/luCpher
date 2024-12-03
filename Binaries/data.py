import sqlite3

con = sqlite3.connect("luCpher.db") # initialize sytem and web commands in sql table
cursor = con.cursor() # Here the cursor will access each row at a time in a sql table

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO sys_command VALUES(null,'vpn','C:\\Program Files\\Proton\\VPN\\ProtonVPN.Launcher.exe')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'w3school', 'https://www.w3schools.com')"
#cursor.execute(query)
#con.commit()

#query = "DELETE FROM web_command WHERE id = 5"
#cursor.execute(query)
#con.commit()


# testing module
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
#desired_columns_indices = [0, 20]




