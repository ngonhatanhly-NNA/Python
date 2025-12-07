import numpy as np
# Fundamental of numpy
matrix = np.array([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]], dtype='U7')
shape = matrix.shape 
dimension = matrix.ndim # (3, 3)
size = matrix.size # 9
dtype = matrix.dtype # int32

# Method in numpy
a = np.full((2, 3, 4), 9)   # shape (2 mat, 3 row, 4 col), fill with value 9
# -> [[ [9 9 9 9]           [9 9 9 9]    
#       [9 9 9 9]           [9 9 9 9]    
#       [9 9 9 9]]          [9 9 9 9]    
a0 = np.zeros((2, 3, 2))   # fill all the element with vector 0
# Similarly with other
a1 = np.ones((1, 1, 1 ))
aemp = np.empty((2, 1, 1)) # don't know how it work yet

#####
x_values = np.arange(0, 1005, 5) # print a list of numbers from 0 -> 1005, gap by 5
x_vals = np.linspace(0, 1000, 4) # how many number, it will return number which have equally separated step

# Operation in numpy, unlike array it will do mathematic operation
# Understand that, i don't want to illustrate it T^T
# Append, extend and insert
matrix = np.append(matrix, [7, 8, 9])
np.insert(matrix, 1, [4, 5, 4])
np.delete(matrix, 1, 0)
# np.reshape -> reshape rows and cols