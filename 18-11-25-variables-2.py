items = []
price = 0 
total = 0
for i in range(4):
    name = input("Enter product name: ")
    items.append(name)
    price = int(input("Enter price: "))
    total = total + price
print("You entered 4 products they were: ")
print(items)
print("Total cost is:",total)