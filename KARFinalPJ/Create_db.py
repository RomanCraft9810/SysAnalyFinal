import sqlite3
conn = sqlite3.connect("database.db")

print("Database connected.")

cmd = "CREATE TABLE rooms (Name TEXT, checkindate TEXT, checkoutdate TEXT, Roomtype TEXT)"

conn.execute(cmd)

print("Table created successfully.")

conn.close()