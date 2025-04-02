import sqlite3

database_file = "sampleDB.db" #replace with database name
table_name = "sampleTamble" #replace with your actual table name

conn = sqlite3.connect(database_file)
cursor = conn.cursor()

cursor.execute(f"SELECT * FROM {table_name};") # Use f-string for table name
rows = cursor.fetchall()

if rows:
    for row in rows:
        print(row) # Print each row as a tuple
else:
    print(f"No data found in table '{table_name}'.")

conn.close()