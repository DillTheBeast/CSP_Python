#Dillon Maltese
#3/2/23
#Exercise 4.2B

#Takes in your name
name = input("Please enter your name: ")
#name is not any value until the user enters a name and then name will be set to whatever the user enters
print("Hello " + name + ".")
#takes in your age
age = input("Please enter your age: ")
age = int(age) + 10
print(name + " you will be " + str(age) + " in 10 years.")