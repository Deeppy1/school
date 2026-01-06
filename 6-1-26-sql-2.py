import sqlite3

connn = sqlite3.connect("tuckshop.db")
cursor = connn.cursor()

sweet = input("Enter sweet name: ")
price = int(input("Enter price in pence: "))

cursor.execute(
    "INSERT INTO tuckshop (sweet, price) VALUES (?, ?)",
    (sweet, price)
)

connn.commit()
connn.close()

print("Sweet added")