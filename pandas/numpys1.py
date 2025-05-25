#what is numpy actually? -> Its just a library for computing, really modeling or data analysis
#an array contains information about raw data, how to locate an element and how to interpet an element

#1d Array -> like a 1 by 3 for example (1 row and three columns)
#2d Array -> can be a 2 by 3 for example (with two axises)
#3d Array -> Self Explanatory (three axises indexed at 0)

import numpy as np 

my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype = np.int64)
#print(my_array)

#Cheat sheet of some code dowb below 

#create arrays 

Dorian = np.array([1,2,3]) #1 by 3 
Dorian1 = np.array([(1.3,2,2.3), (5,6,7)], dtype = float) #2 by 3
Dorian2 = np.array([(1.3, 2.3, 4), (5, 7, 8), (9,0,9)], dtype = float) #3 by 3 

#print(Dorian, Dorian1, Dorian2)

#initial Placeholders 

zin = np.zeros((3,4)) #an array of zeros a 3 by 4 (3 rows 4 columns)
print(zin)
xin = np.ones((2,3,4), dtype = np.int16) #an array of ones, 2 blocks each a 3 by 4 
#print(xin)
yin = np.arange(10,25,5) #array of evenly spaced values (number of samples) or it makes an array of x values (if it is one value)
#print(yin) #10, 15, 20 (based on start, stop, step method), arange not ARRANGE

ain = np.linspace(0,2,5)
#print(ain) #evenly spaced values (based on number of samples, the end number will be the total number in the output)
#the increments are just the perfect amount to get to the middle number given the end number 

bin = np.full((2,2),7) #so these are two, two by twos populated with seven
#print(bin)

cin = np.eye(3,10)
#print(cin) #here this makes an x by x identity matrix (given one value), where the first and last numbers in the matrix are 1

#if this was a y by x then we start with a 1 (up until x value)
#and then next row starts at 0, then will fill a 1 based on the value in y
#so a 2,10 is just 1 starting 1st row, then second row starts 0 and then 1

din = np.random.random((2,2))
#print(din) #makes a 2 by 2 with random values (within that range of 2?)

ein = np.empty((3,2))
print(ein) #on looks np.empty and np.zeros appear to do the same thing

#why are Initial placeholders important?
#good for efficiency and avoid resizing, avoids unintended values with things like empty and zeros
#good for code clarity as well b/c we define our stuff even if we don't know what to do with it 

#How to add and combine series

s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20], index=['d', 'e'])

combined = pd.concat([s1, s2])
print(combined) #via concatenating

#via adding

stest1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
stest2 = pd.Series([10, 20], index=['a', 'b'])

combined = stest1.add(stest2, fill_value=0)
print(combined)

#combnine by position

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([10, 20])

combined = pd.Series(list(s1) + list(s2))
print(combined) 

#main ways to combine series -- which work the same way for dataframes just need to be more wary of rows and columns

