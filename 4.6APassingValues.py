#Dillon Maltese
#4.6A

import random
names = []

def compare(input1, input2):
    if(input1 < input2):
        print(str(input1) + " is less than " + str(input2))
    elif(input1 > input2):
        print(str(input1) + " is greater than " + str(input2))
    elif(input1 == input2):
        print(str(input1) + " is equal to " + str(input2))
    else:
        print("This should not happen")

def eliminate(vote, names):
    for i in range(vote):
        random.shuffle(names)
        names.pop()
    return names

for i in range(3):
    input1 = int(input("Pick a number: "))
    input2 = int(input("Pick a second number: "))
    compare(input1, input2)
    
for i in range(6):
    name = input("Please enter a name: ")
    names.append(name)

vote = int(input("Enter the amount of people that you would like to vote off of the island: "))
eliminate(vote, names)
print("The people remaining are:")
for i in names:
    print(i)