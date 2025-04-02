import sqlite3

database_file = "sampleDB.db"

conn = sqlite3.connect(database_file)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

if tables:
    print("Tables in the database:")
    for table in tables:
        print(table[0])
else:
    print("No tables found in the database.")

conn.close()