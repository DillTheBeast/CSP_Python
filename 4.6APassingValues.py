#Dillon Maltese
#4.6A

def compare(input1, input2):
    if(input1 < input2):
        print(str(input2) + " is greater than " + str(input1))


for i in range(3):
    input1 = int(input("Pick a number: "))
    input2 = int(input("Pick a second number: "))
    compare(input1, input2)