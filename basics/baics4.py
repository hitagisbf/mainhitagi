#this will be the notes for the "For" loop, for is just for iteration purposes, see below
for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")
#this takes a list of names and prints them over and over with a special message for each 
#we can use for in conjunction with range to add to our iteration purposes
#see the below code to print something 50 times

for i in range(50):
    print('Syn Shenron: I will end your suffering.')

#three ways this works: Range(stop), Range(start, stop), Range(start, stop, step#)
#range(5) -> 0,1,2,3,4
#range(2,5) -> 2,3,4 -> excludes the last number
#range(1,10,2) -> 1, 3, 5, 7, 9 -> start at 1 increment by 2 
#as we see above we see range in a loop to repeat something multiple times
print(list(range(4))) #list gives it that bracket look 
#next (in this section will be the conditional stuff )
#if boolean: 
    #statement_1 -> done if condition is true
#else:
    #statement_2 -> done if condition is false
#the if will print statement 1 if statement 1 is true, and if it is not
#then it will skip over the block and then execute the false statement

#see
if 4 + 5 == 10:
    print('Good math')
else:
    print('Bad Math')

#we don't always need an else statement, and if we do not have one
#the statement will always print the true statement or follow the if statement

x = -1
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed")
#when there is no else statement then python will execute the body of the if block 
#and the other statement that follows the if block 
#the other thing is that every else block must be paired with an if block 
#we can chain them but you can't have two else blocks and one if block for example


#NOTE IT CANNOT BE TWO ELSE STATEMENTS IN THE SAME BLOCK
#x = -10
#if x < 0:
    #print("The negative number ",  x, " is not valid here.")
#else:
   #print(x, " is a positive number")
#else:
   #print("This is always printed")

#however the below is correct

letter = 12
sentence = 15
if letter > sentence:
    print("letter is better than sentence")
else:
    if letter < sentence:
        print("text")
    else:
        print('final')


#chaining conditionals with elif 

#elif just means else if, and we can have a whole bunch of else if's 
#but we can only have one final else in our statement this way

a = 10
b = 15
if a > b:
    print("a is better than b")
elif a < b:
        print("a is worse than b")
else:
    print("everything is bad")

#think if all else fails with the ifs and the else if's then the else will be executed as the last true thing 

        
    