import numpy as np
from string import ascii_uppercase


dorian = np.array([1,2,3,5,6])
xin = np.array([1,2,0,5,6])
#print("Original array is:")
#print(dorian)

print(np.all(dorian)) #this part prints out a true saying that none of them are zero
print(np.all(xin))

Dorian4 = np.array([(1.3, 2.3, 4), (5, 7, 8), (9,0,9)], dtype = float)
#Dorian5 = np.zeros([3,3])
dorian6 = np.identity(3)

#print(dorian6)

arange = np.arange(10)
print(arange)
arange2 = np.random.rand(3,10)
#print(arange2)

bin = np.random.randint(1,6,10) #random and then randint for generation
#print(bin)

dtype = [('name', 'U12'), ('age', 'i4'), ('height', 'f4')]

structured_array = np.array([
    ('Lehi Piero', 25, 5.5),
    ('Albin Achan', 30, 5.8),
    ('Zerach Hava', 35, 6.1),
    ('Edmund Tereza', 40, 5.9),
    ('Laura Felinus', 28, 5.7)
], dtype=dtype)

structured_array['name'] = 'Dorian'

#for name in structured_array['name']:
    #print(name)

test = np.array(chr(i) for i in range(ord('A'), ord('z')))
#print(test)

a = np.array(list(ascii_uppercase))

#print(a)

dim_test = np.arange(1,10,2)
print(dim_test.ndim)

new_dim_test = dim_test.reshape(5,1)
print(new_dim_test)
print(new_dim_test.ndim)

print_final_dim = new_dim_test.reshape(1,3)
print(print_final_dim)