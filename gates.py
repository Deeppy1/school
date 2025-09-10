#maths operators in python
import math
import time
def main_menu():
    operator_selection=input("""===Python Calculator===
1. Addition
2. Subtraction
3. Multiplication
4. Devision
5. Square Root
Please make your Selection: """)
    operator_selection=int(operator_selection)
    if (operator_selection == 1):
        add()
    elif(operator_selection == 2):
        subtract()
    elif(operator_selection == 3):
        multiply()
    elif(operator_selection == 4):
        divide()
    elif(operator_selection == 5):
        sqrt()
    else:
        print("Please enter 1-5")
        main_menu()    

def add():
    in_a=input("Please enter your first number: ")
    in_b=input("Please enter your Seccond Number: ")
    in_a = int(in_a)
    in_b = int(in_b)
    output_a = in_a + in_b
    output_a=str(output_a)
    print("Answer = "+output_a)
    time.sleep(0.5)
    main_menu()
def subtract():
    in_a=input("Please enter your first number: ")
    in_b=input("Please enter your Seccond Number: ")
    in_a = int(in_a)
    in_b = int(in_b)
    output_a = in_a - in_b
    output_a=str(output_a)
    print("Answer = "+output_a)
    time.sleep(0.5)
    main_menu()
def multiply():
    in_a=input("Please enter your first number: ")
    in_b=input("Please enter your Seccond Number: ")
    in_a = int(in_a)
    in_b = int(in_b)
    output_a = in_a * in_b
    output_a=str(output_a)
    print("Answer = "+output_a)
    time.sleep(0.5)
    main_menu()
def divide():
    in_a=input("Please enter your first number: ")
    in_b=input("Please enter your Seccond Number: ")
    in_a = int(in_a)
    in_b = int(in_b)
    output_a = in_a / in_b
    output_a=str(output_a)
    print("Answer = "+output_a)
    time.sleep(0.5)
    main_menu()
def sqrt():
    in_a=input("Please enter your first number: ")
    in_a = int(in_a)
    output_a = math.sqrt(in_a)
    output_a=str(output_a)
    print("Answer = "+output_a)
    time.sleep(0.5)
    main_menu()



main_menu()