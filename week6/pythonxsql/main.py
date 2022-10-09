import psycopg2
from config import host, user, password, db_name


try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name    
    )
    connection.autocommit = True
    
    # the cursor for perfoming database operations
    # cursor = connection.cursor()
    #create a new table
    #with connection.cursor() as cursor:
        #cursor.execute(
            #"""CREATE TABLE users(
                #id serial PRIMARY KEY,
                #id_number varchar(50) NOT NULL,
                #first_name varchar(50) NOT NULL,
                #gender varchar(50) NOT NULL,
                #nationality varchar(50) NOT NULL,
                #nick_name varchar(50) NOT NULL);"""
                #)
    
    #insert data into a table
    #with connection.cursor() as cursor:
        #cursor.execute(
            #"""INSERT INTO users (id_number, first_name, gender, nationality, nick_name) VALUES
            #('212060', 'Abylkair', 'Male', 'Kazakh', 'AbL1GhT' );"""
        #)
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        
        print(f"Server version: {cursor.fetchone()}")
        
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")