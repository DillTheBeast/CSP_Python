#Dillon Maltese
#4.4 Exercise A Part 3

amount = int(input("How many numbers would you like to add? "))
#array stores all of the input numbers
numToAdd = []

#numAmount is however many numbers he would like to add
numAmount = amount
num1 = 0
#x and y are place holders for the array
x = 0
y = 0

#While loop will run however many times the user wanted to add the numbers
for x in range(numAmount) :
    num = int(input("What is the number you would like to add "))
    #Adds each input number into the array
    numToAdd.append(num)
    x+= 1
    
#Repeats for the length of array
for y in range(x) :
    #num1 takes all of the numbers and adds them
    num1 = num1 + numToAdd[y]

print("The number is " + str(num1));