#selection(if statements)
import time
score = 0
x = 0
questions = ["What is the capital of London: ","What is the capital of Australia: "]
answers=["l","canberra"]
for i in questions:
    answer = input(i).lower()
    print(answers[-x])
    if answer == (answers[-x]):
        print("correct")
        score+=1
    else:
        print("wrong")
        score-=1
    x+=1