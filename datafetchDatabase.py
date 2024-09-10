# # importing mysql.connector - an api to connect to localhost mysql database
# import mysql.connector

# # creating a database connection object 
# try:
#     mydb = mysql.connector.connect(
#             host = "localhost",
#             user = "root",
#             database = "your database",
#             password = "your password"
#             )
#     # checking if the connection is made successfully or not,
#     #  if it does it returns a connection object in mydb
#     if mydb.is_connected():
#         print("Connection Successfull with connection string - ",mydb)
# # else catching the raise exception of not being able to connect
# except mysql.connector.Error as C:
#     print(f"Coudn't connect to database! - {C}")

# finally:
#     # once the connection to the database is made successfully 
#     # we can perform tasks on database and table as required
#     # using a cursor to interact with database
#     cursor = mydb.cursor()      #creating a cursor
#     # query = "SHOW TABLES;"      # writing a query to execute
#     # cursor.execute(query)       # executing the query using cursor

#     # tables = cursor.fetchall()  # collect results of statement using fetchall 
#     # print(tables)
#     # or it can be looped to print the tables clearly
#     # for table in tables:
#     #     print(table)

#     # another query
#     query = "SELECT * FROM PERSON;"
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     # printing all the rows fetched from database
#     for row in rows:
#         print(row)
    
#     # rest of the things can be manipulated as required
#     if mydb.is_connected():
#         cursor.close()
#         mydb.close()
#         print("Connection to the database is closed.")



import mysql.connector
from mysql.connector import Error

try:
    # Creating a database connection object
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="your database name",
        password="your password"
    )
    
    # Checking if the connection is made successfully or not
    if mydb.is_connected():
        print("Connection Successful with connection string -", mydb)
    
except Error as e:
    print(f"Couldn't connect to database! - {e}")

else:
    # Using a cursor to interact with the database
    cursor = mydb.cursor()

    try:
        # Example query to fetch data from PERSON table
        query = "SELECT * FROM PERSON;"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Printing all the rows fetched from the database
        for row in rows:
            print(row)

    except Error as e:
        print(f"Error executing query! - {e}")

    finally:
        # Closing the cursor and connection
        cursor.close()
        mydb.close()
        print("Connection to the database is closed.")

