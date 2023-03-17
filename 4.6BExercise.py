#Dillon Maltese
#4.6B Exercise

import random

guessed = false
counter = 0

rnum1 = random.randint(1,9)
rnum2 = random.randint(1,9)
rnum3 = random.randint(1,9)
rnum4 = random.randint(1,9)

print("Welcome to Code Breaker. \nThe objective of the game is to break the code. \nThe code will be 4 numbers.")

while(guessed == false):
    g1 = false
    g2 = false
    g3 = false
    g4 = false
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))
    num4 = int(input("Enter number 4: "))

    if(rnum1 == num1):
        print("The first number that you guessed, " + str(num1) + ", is correct")
        g1 = true
    if(rnum2 == num2):
        print("The first number that you guessed, " + str(num1) + ", is correct")
        g2 = true
    if(rnum3 == num3):
        print("The first number that you guessed, " + str(num1) + ", is correct")
        g3 = true
    if(rnum4 == num4):
        print("The first number that you guessed, " + str(num1) + ", is correct")
        g4 = true
    if(g1 == g2 == g3 == g4 == false):
        print("Sorry you got nothing correct")
    if(g1 == g2 == g3 == g4 == true):
        print("Nice job, you have won. \nThe secret number was " + str(rnum1) + str(rnum2) + str(rnum3) + str(rnum4) + "\nIt took you " + str(counter) + " tries")
        guessed = true
    counter += 1

