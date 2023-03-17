#Dillon Maltese
#4.6B Exercise

import random

guessed = False
counter = 0

rnum1 = random.randint(1,9)
rnum2 = random.randint(1,9)
rnum3 = random.randint(1,9)
rnum4 = random.randint(1,9)

print(str(rnum1) + str(rnum2) + str(rnum3) + str(rnum4))
print("Welcome to Code Breaker. \nThe objective of the game is to break the code. \nThe code will be 4 numbers.")

while(guessed == False):
    g1 = False
    g2 = False
    g3 = False
    g4 = False
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))
    num4 = int(input("Enter number 4: "))

    if(rnum1 == num1):
        print("The first number that you guessed, " + str(num1) + ", is correct")
        g1 = True
    if(rnum2 == num2):
        print("The second number that you guessed, " + str(num2) + ", is correct")
        g2 = True
    if(rnum3 == num3):
        print("The third number that you guessed, " + str(num3) + ", is correct")
        g3 = True
    if(rnum4 == num4):
        print("The fourth number that you guessed, " + str(num3) + ", is correct")
        g4 = True

    if(g1 == g2 == g3 == g4 == False):
        print("Sorry you got nothing correct")

    counter += 1
    
    if(g1 == g2 == g3 == g4 == True):
        print("Nice job, you have won. \nThe secret number was " + str(rnum1) + str(rnum2) + str(rnum3) + str(rnum4) + "\nIt took you " + str(counter) + " tries")
        guessed = True

