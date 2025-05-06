#Boolean Basics 

#True and False are booleans (not true and false (the lowercase))
#Booleans are not strings they are just part of the bool class

#Two Boolean expressions (== not = as one = is for assignment purposes)
print( 6 == 7)
print( 8 == 8)

test = 5
print(test > 7 or test < 10)
print(test % 5 == 1 and test % 2 == 1)

phone_health = 10
twophone_health = 17

if phone_health <= 15 and twophone_health <=16:
    print("Phone is dying...")
else:
    print("phone is good")
    
#We know If and else is the backbone of Booleans however there are unary if statements
#Unary meaning we omit the else statement in place if one if statement, where it will print the statement if true
#and does nothing if false (like the code below)

x = 10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
    
#If statements would not be complete without the idea of nesting, since we have done this so many times in excel 

x = 10
y = 10

if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x and y must be equal")

#Since X and Y are equal this prints the last else statement (since they are both the same)
#Just note the nesting done here with the necessary indentations 

#elif -> is just else if with less words, does the same thing and needs that end else box 

x = 10
y = 10

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")
    
#No limit to the amount of elifs one can use 

#We have learned how to define functions to print things but we can also define functions to return booleans instead
#This comes from an == perspective 

def doriandivisible(x,y):
    if x%y == 0:
        result = True
    else:
        result = False
    
    return result

print(doriandivisible(8,4))

#Test problems

#Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

def is_even(n):
    if n%2 == 0:
        result = True
    else:
        result = False
    
    return result #always return the result in defined functions or it will print none

print(is_even(4))

#Now write the function is_odd(n) that returns True when n is odd and False otherwise.

def is_odd(n):
    if n%2 != 0:
        result = True
    else:
        result = False
    return result

print(is_odd(6))


#Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

def is_rightangled(x,y,z):
    if x+y+z == 180: #remember == for comparison not assigment 
        result = True
    else:
        result = False
    return result

print(is_rightangled(10,20,40))

#The other way to do this was to use the pythagorean theorem

def sec_is_rightangled(x,y,z):
    return abs(x**2 + y**2 - z**2)

print(sec_is_rightangled(14,15,16))

#We define a leap year as 

#The year is evenly divisible by 4;

#If the year can be evenly divided by 100, it is NOT a leap year, unless;

#The year is also evenly divisible by 400. Then it is a leap year.

#Knowing this write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.

def is_loopyear(year):
    
    if year%4 == 0 and (year%100 != 0 or year%400 ==0):
        result = True
    else:
        result = False
    return result

print(is_loopyear(2024))
    
    
    
    
