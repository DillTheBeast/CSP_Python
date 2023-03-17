#Dillon Maltese
#4.6A

def compare(input1, input2):
    if(input1 < input2):
        print(str(input1) + " is less than " + str(input2))
    elif(input1 > input2):
        print(str(input1) + " is greater than " + str(input2))
    elif(input1 == input2):
        print(str(input1) + " is equal to " + str(input2))
    else:
        print("This should not happen")


for i in range(3):
    input1 = int(input("Pick a number: "))
    input2 = int(input("Pick a second number: "))
    compare(input1, input2)