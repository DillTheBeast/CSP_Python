#Dillon Maltese
#Exercise 4.5

names = ["Peter", "Bruce", "Steve", "Tony", "Natasha", "Clint", "Wanda", "Hope", "Danny", "Carol"]
numbers = ["100", "50", "10", "1", "2", "7", "11", "17", "53", "-8", "-4", "-9", "-72", "-64", "-80"]


y = 0
x = 0
z = 0
a = 0
b = 0
j = 0
o = 0
place = 0
#Every other name
print("Every other name")
while(y < len(names)) :
    print(names[y])
    y = y + 2
    
#Only positive numbers in numbers list
print("All positive numbers")
for i in numbers:
    if(int(numbers[x]) > 0 ) : 
        print((numbers[x]))
    x+=1

#Sum of all values
print("Sum of all values")
for i in numbers:
    z = z + int((numbers[a]))
    a+=1
print(z)

#Only odd numbers
print("All odd values")
for i in numbers:
    if(int(numbers[b]) % 2 == 1):
        print(numbers[b])
    b+=1
    
#Names that come before Thor
print("Names that come before Thor in the alphabet")

for i in names:
    for p in names[j]:
        first = names[o]
    place = ord(str(first))
    print(place)
    j+=1



