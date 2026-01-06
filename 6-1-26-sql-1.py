import sqlite3

conn = sqlite3.connect("tuckshop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE tuckshop (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
sweet TEXT,
price INTIGER
)
""")

conn.commit()
conn.close()

print("DB created")