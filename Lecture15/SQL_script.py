#!/usr/bin/python3

import MySQLdb

def get_table_choice(host, user, password, database):
    """
    Queries the database for all available tables and prompts the user to select one.
    Returns the string name of the chosen table, or None if exit/error.
    """
    connection = None
    try:
        connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database
        )
        cursor = connection.cursor()
        
        # 1. Fetch all tables in the database
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        
        if not tables:
            print("No tables found in this database.")
            return None

        # 2. Display the tables as a numbered menu
        print("\nAvailable Tables:")
        print("-" * 30)
        for index, table_name in enumerate(tables, 1):
            print(f"[{index}] {table_name}")
        print("-" * 30)
        
        # 3. Handle user selection input safely
        while True:
            try:
                choice = input(f"Pick a table number (1-{len(tables)}) or 'q' to quit: ").strip()
                if choice.lower() == 'q':
                    return None
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(tables):
                    return tables[choice_num - 1]
                else:
                    print(f"Invalid number. Please choose between 1 and {len(tables)}.")
            except ValueError:
                print("Please enter a valid number or 'q'.")

    except MySQLdb.Error as e:
        print(f"Database error while fetching tables: {e}")
        return None
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()

def describe_mysql_table(host, user, password, database, table_name):
    """
    Connects to a MySQL database and prints the layout structure of a specified table.
    """
    if not table_name:
        return

    connection = None
    try:
        connection = MySQLdb.connect( host=host, user=user, passwd=password, db=database )
        cursor = connection.cursor()

        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()

        print(f"\nStructure for table: '{table_name}'")
        print("-" * 65)
        print(f"{'Field Name':<20} | {'Type':<18} | {'Null?':<6} | {'Key':<5} | {'Default'}")
        print("-" * 65)
        
        for col in columns:
            field, data_type, null_allowed, key, default, extra = col
            default_val = default if default is not None else "NULL"
            print(f"{field:<20} | {data_type:<18} | {null_allowed:<6} | {key:<5} | {default_val}")
        print("-" * 65)

    except MySQLdb.Error as e:
        print(f"Failed to describe table '{table_name}': {e}")
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    # Define your connection credentials once
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASS = "your_password"
    DB_NAME = "your_database_name"

    # Step 1: Prompt the user to pick a table from the menu
    chosen_table = get_table_choice(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    
    # Step 2: Describe the chosen table
    if chosen_table:
        describe_mysql_table(DB_HOST, DB_USER, DB_PASS, DB_NAME, chosen_table)
    else:
        print("Exiting table viewer.")
