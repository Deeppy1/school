total = 0
family = [["Bart", 10],["Homer",40],["James",13],["John",30]]
for name,age in family:
    #print(name,"is",age,"years old")
    if age < 12:
        cost = 30
    else:
        cost = 50
    print(name,"will habe to pay",cost)
    total +=cost
print("your total is:",total)