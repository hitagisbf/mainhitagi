#Functions part two, since functions can call on other functions
#see the below example

def square(x):
    y = x*x
    return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)
    
    return a + b + c

a = -5
b = 2
c = 10
result = sum_of_squares(a, b, c)
print(result)

#this defines square as y = a squared number and then sum of squares
#is just the square function over over and over for different variables 
#where we return a + b + c, b/c thats what we will end up doing 
#so its -5*-5 + 2*2 + 10*10 which is 129

#We will go over how python iterates or executes the statements in the defined function
def pow(b,p):
    y = b ** p
    return y 

def square(x):
    a = pow(x,2)
    return a

n = 5 
result = square(n)
print(result)

#the order that python will evaluate this is (fron lines 27-37)
#27, 31, 35, 36, 31, 32, 27, 28, 29, 32, 33, 37
#we start from the top, and then read the other defined function
#then if there are global parameters we read that, and read what is being done to it
#Then since this calles square (35) we go back to the square function
#then we execute the function, which calls pow, which is in 27 (reads that)
#and then it reads the conditions of pow all the way down to 29, then back to where it is called again
#and then returns it and then prints the result

#The main Function 

#The main function is not a special feature but really a clever name that we use for simplicity
#which serves as the starting point in our program
#there is a python interpreter built in that chooses a few special variables, one of those being _name_
#_name_ is automatically set to the string "_main_" when the program is being called by itself
#however, in the case that we import a module, _name_ is set to the name of that module 

#Take the below functions

def squareit(n):
    return n * n
def cubeit(n):
    return n*n*n
def main():
    anum = int(input("enter a number:"))
    print(squareit(anum))
    print(cubeit(anum))

if __name__ == "__main__":
    main()
    
def main():
    print("Hello from main!")

if __name__ == "__main__":
    main()

