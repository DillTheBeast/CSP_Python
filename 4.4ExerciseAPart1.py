#Dillon Maltese
#4.4 Exercise A part 1


isCorrect = False

while(isCorrect == False):
    number = int(input("Please enter a number between 1 - 100 "))
    if(number >= 1 and number <= 100) :
        print("Thank you for your input")
        isCorrect = True
    else :
        print("This is not an option")
        