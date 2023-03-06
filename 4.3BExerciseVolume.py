#Dillon Maltese
#4.3B Part 2

import random

pi = 22/7
r1 = float(input("Enter a small decimal number "))
r2 = float(input("Enter a large decimal number "))
r = float(random.uniform(r1, r2))

v = float(4/3*pi*(r)**3)
print("The volume of the sphere with the radius:" + str(r) + " is: " + str(v))