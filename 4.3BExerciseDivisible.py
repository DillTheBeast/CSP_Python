#Dillon Maltese
#4.3B Part 1


#Taking in a name
name = input("Please enter your name: ")
#Taking in a number
number = int(input(name + " Please enter a number "))
#taking in a number to divide the other number by
divider = int(input(name + " Please enter another number "))

#if number 1 mod number 2 is 0, then they will always divide to get a whole number
if number % divider == 0:
    print(str(number) + " is not divisible by " + str(divider))
    
#This will run if number 1 mod number 2 is not = to 0
else:
    print(str(number) + " is divisible by" + str(divider))