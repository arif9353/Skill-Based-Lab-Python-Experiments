#Program to create a SQLITE3 database
import sqlite3

#db creation
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

#table creation
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER)''')

#insertion
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('ARIF', 20))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('PRAJWAL', 30))
conn.commit()

#Printing values from DB
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

#Updating
cursor.execute("UPDATE students SET age = 31 WHERE name = 'Bob'")
conn.commit()
conn.close()
