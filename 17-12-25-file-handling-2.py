with open("17-12-25.txt","r") as file:
    content = file.readlines()
    line = content[3]
    print(line.strip())
