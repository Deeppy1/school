print("Unicode info")
for i in range(55296):
    base2=bin(i)
    hex2 = hex(i)
    print("Unicode value:",i,"is:",chr(i),"Binary:",(base2[2:]),"Hex:",(hex2[2:]))
