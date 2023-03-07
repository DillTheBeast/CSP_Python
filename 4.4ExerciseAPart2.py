#Dillon Maltese
#4.4 Exercise A Part 2

favColorCap = "blue"
favColorLow = "Blue"
guessRight = False

while(guessRight == False) :
    guess = input("Guess my favorite color ")
    if(guess == favColorCap or guess == favColorLow) :
        print("Nice Job")
        guessRight = True
    else :
        print("Wrong")
    