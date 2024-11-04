#this will be a continuation of variables, really starting with input
#input our fav function ever, is literally designed for user input 

test = input("enter your name: ")
print("I will end your suffering:", test)

#so here input has as enter a name and then we print something arbitray along with 
#the user input denoted by test
#input by default returns string, so if you wish for it to be a float or integer
#you must change the type like we did in basics 1, with something like str(3.14)
str_seconds = input("Please enter the number of seconds you wish to convert: ")
total_secs = int(str_seconds) #turns the string from input into integer

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining) 
#here we call string forms along with our variables to allow this to work 
#note the types of strings here
#str_seconds is a string (by input) 
#but hours and everything below that are integer 
#variable types are denoted by their output (a text variable is a text variable because it spits out string)
# a small note on reassignment, we have seen that when one variable is called multiple times and then printed 
#it will have printed out the last denoted thing of that variable
#down below is an example of reassignment 
a = 5
b = a 
print(a,b) #at this point a and b are both equal, as they both print 5 
a = 3 
print(a,b) #here we can see that reassigning a, changes it's initial value 
#but not the value of b which is still 5, due to its first assignment 
#this excercise consolidates the idea of printing the last value and updating values as we go 
#see 
x = 6        # initialize x
print(x)
x = x + 1    # update x
print(x) # which will print 7 as the final iteration 

#we can only update variables once they have been called so see 
Dorian_balance = 120
Dorian_balance = 120 + 55
print(Dorian_balance) #which will print 175 b/c we call the variable and then update it 
#for Bloomberg -> Write a program that will convert degrees fahrenheit to degrees celsius.

