print("===Welcome to the Storage quiz===")
seccondary=['hdd','ssd','cd']
primary=['ram','rom']
primarya=['volatile','non-volatile']
score = 0
q1 = input("What is a type of primary storage? ").lower()
if q1 in primary:
    score += 1
    print("Well done that is correct your score is",score)
else:
    print("Sorry that wasn't quite right")
q2 = input("How many bits in a nibble? ")
if q2 == "4":
    score += 1
    print("Well done that is correct your score is",score)
else:
    print("Sorry that wasn't quite right")
q3 = input("true or false: Binary is the language used for commputers? ").lower()
if q3 == "true":
    score += 1
    print("Well done that is correct your score is",score)
else:
    print("Sorry that wasn't quite right")
q4 = input("Is Ram volatile or non-volatile? ")
if q4 == "volatile":
    print("Correct RAM is volatile")
    score += 1
q5 = input("Is rom volatile or non-volatile? ")
if q5 == "non-volatile":
    print("Correct rom is non-volatile")
    score += 1
q6 = input("""What is the missing word "magnetic, solid state, _______? """).lower()
if q6 == "optical":
    print("Correct rom is non-volatile")
    score += 1
q7 = input("").lower()
if q6 == "optical":
    print("Correct rom is non-volatile")
    score += 1