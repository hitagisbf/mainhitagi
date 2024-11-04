#start of variables and mathematics 
message = "What's up, Doc?"
n = 17
pi = 3.14159
#here we just defined three variables, nothing more nothing less 
#also note = here being for definition not for equality (==)
print(message)
print(n)
print(pi)
print(message,n,pi)
#we see one iteration of this does this on different lines while the last iteration
#does this all on one line, the important thing is that it will print whatever is called last
#see this example
bill = "bill"
bill = 95
bill = "fifty ball"
print(bill)
#here we can see it calls the last bill, not all the "bill's"
#when making variable names don't use spaces use underscores and don't use some of pythons keywords
#similar to using value in excel and using "id" in the security part, python doesnt permit certain things as well
#some include class, and, as, assert, while, yield, etc
#rule of thumb just use unique names 
#going to include some statements here such as len, while, for, if, and import 
print(len('dorian reece')) #returns the length of characters, not letters
# + is addition, - is subtraction
# * is multiplication, ** is exponentiation, () work just as in math 
# // is integer division which results in the next smallest integer
# / is regular division which can return a float 
# % modulo which returns the remainder in division, useful to see if another number is divisible by another
# when we see divisible we mean the remainder is zero, which can be useful in some analysis
minutes = 750
total = minutes/60
print(total ) #two variables one in the other, where we print the final 
print(6/4) # no rounding done here 
print(6//4) # rounds 1.5 to 1 
print(7%3) #returns 1 
print(8%3) #returns 2
print(18%4) #returns 2
