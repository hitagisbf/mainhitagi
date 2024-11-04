#Section on defining functions and what they mean
#a function is just a sequence of statements that go together 
#something like 
#def name ( x y z ):
#statements 

#example with math 

import math
print(math.pow(2,3)) #this is 2 to the third power 
print(max(7,11)) #prints the max in a set of arguments or list

#our first defined function (here y is a local variable, but the script runs as square runs)

def square(x):
    y = x * x
    return y 

toSquare = 10
result = square(toSquare)
print("The result of ", toSquare, "squared is", result)

#one may ask "how does this execute when x is never called again?"
#the answer is that because we defined this function globablly its as if x = tosquare
#global variables (variables defined outside of any function)
#after we have the return function nothing else should exist in that box
#meaning it is the last part of our defining function, so it must be there
#no return means nothing will happen (which is a bad thing)
#note we always end up calling back the original function in our other box there

#example 
def square(x):
#raise x to the second power
    return x*x

print('testing square function')
assert square(3) == 9
#a run time error would occur here if this was 4 instead of 3 for example
#this just takes 3*3 b/c square is x*x

#what does assert here really do? Assert is just a way to test something 
#where after assert there will be a python expression, where False returns a run time error
#and the correct code does nothing and keeps executing the code as normal
#good for testing our code when we are first building it out
#for example assert x == y, will do nothing (granted x and y are equal)
#and just execute the rest of the code

#example 2 (number is also a local variable)

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

num = int(input("Enter a number: "))
result = check_even_odd(num)
print(result)

#can read this bottom up, where we the result is the condition of the defined function
#wrapped around the variable we called "num", so basically our final thing just executes the function
#and returns whatever is necessary

#the main takeaway I want is the methodology of defining a function
#DO NOT DO 

#def square(x):
    #y = x*x
    #return(y)
#a = square(8)
#print(y)

#do not return a variable and then use it in the same block to execute, because the assignment statement is local
#so you cannot use it outside of the block, instead do 

def square(z):
    y = z*z
    z = 5
    return(y)

z = 4
a = square(z)
print(a)

#this is a good example of a local and global variable, where z here is locally defined
#and then globably defined allow us to reuse it 
#define the function assigning z to 5 
#reassign z to another value since we can't just not call it
#a = square which is y = z*z or in other words here 
#a = 4*4 b/c the reassignment

b = 7
def test():
    global b
    print(b)
    b+=6
    print(b+5)

test()

#this is a global variable b, meaning it can be used outside that script 


