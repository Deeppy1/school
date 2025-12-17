with open("17-12-25.txt","r") as file:
    content = file.read()
    words = content.split()
    print(words)
    count = len(words)
    print(count)