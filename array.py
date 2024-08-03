import numpy as np
#Write a NumPy program to convert a list of numeric values
#into a one-dimensional NumPy array

#NumPy one-dimensional array: linear data structure, 
# similar to a list. It has elements of the same type, arranged in a single line.
l = [12.23, 13.32, 100, 36.32]
a = np.array(l)

#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
x = np.arange(2,11).reshape(3,3)

#Write a NumPy program to create a null vector of size 10 and update the sixth 
# value to 11.
array = np.zeros(10)
array[6] = 11

#Write a  NumPy program to create an array with values ranging from 12 to 37.
x = np.arange(12,38)

#Write a  NumPy program to reverse an array (the first element becomes the last).
x = np.arange(12,38)
x = x[::-1]

#Write a  NumPy program to convert an array to a floating type.
x = np.arange(1,3)
x = x.astype(float)

#Write a  NumPy program to create a 2D array with 1 on the border and 0 inside.
array = np.ones(25).reshape(5,5)
array[1:4,1:4] = 0

#Write a NumPy program to add a border (filled with 0's) around an existing array.
x = np.ones((3, 3))
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
#pad_width:Sets the amount of padding to be added to all edges of the matrix. 
# A pad_width of 1 adds a row/column of padding around the entire matrix.
#mode: 'constant' means that the padding will be done with a constant value.
# constant_values: value of the border

#Write a  NumPy program to create an 8x8 matrix and fill it with a checkerboard pattern.
x = np.zeros((8, 8))
#odd lines
x[1::2, ::2] = 1
#even lines
x[0::2, 1::2] = 1

#Write a  NumPy program to convert a list and tuple into arrays.
l = [1,2,3,4,5,6,7,8]
array = np.asarray(l)

t = ([8, 4, 6], [1, 2, 3])
array = np.array(t) #or np.asarray(t)
print(array)
