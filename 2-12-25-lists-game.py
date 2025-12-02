import random
score = 0
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
random.shuffle(numbers)
r1 = input("Will the next number be higher or lower than 5? (1 is higher 0 is lower): ")
print(numbers[0])
if 5 - numbers[0] >= 0 and r1 == 0:
    print("Correct the number was",numbers[0],"you gained 1 point")
    score = score + 1 
else:
    print("Wrong The number was",numbers[0])
    score = score - 1
numbers.remove(numbers[0])
print("BEFORE LOOP BEGIGN")
for i in range(len(numbers)):
    print(i)
    r2 = input("Will the next number be higher or lower than "+str(numbers[i])+" (1 is Higher 0 is Lower): ")
    if numbers[i] - numbers[i+1] >= 0 and r2 == 0:
        print("Correct the next number is",str(numbers[i]),"you gained a point")
        score = score + 1
    else:
        print("Wrong You lost a point the number was: "+str(numbers[i]))
        score = score - 1
print("You score is:",score)