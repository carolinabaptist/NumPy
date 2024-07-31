# Write a NumPy program to get the Numpy version and show the Numpy build configuration
import numpy as np
def getVersion():
    print(np.version.version)
    print(np.show_config())
    return

#Write a NumPy program to get help with the add function.
def getHelp():
    print(np.info(np.add))
    return

#Write a NumPy program to test whether none of the elements of a given array are zero. 

def isZero(a):
    print(np.all(a))
    return

#Write a NumPy program to test if any of the elements of a given array are non-zero. 

def isNonZero(b):
    bool_array = b != 0
    if False in bool_array:
        return True
    return False

def isNonZeroTwo(b):    
    return np.any(b)

#Write a  NumPy program to test a given array element-wise for finiteness (not infinity or not a number).

#array = np.array([1, 2, np.inf, -np.inf, 0, np.nan])

def isInf(array):
    if True in np.isinf(array):
        return True
    return False

def isNan(array):
    if True in np.isnan(array):
        return True
    return False

#Write a NumPy program to test elements-wise for positive or negative infinity. 
def isInfPosNeg(array):
    if True in np.isposinf(array) or True in np.isneginf(array):
        return True
    return False

#Write a NumPy program to test element-wise for complex numbers, real numbers in a given array. Also test if a given number is of a scalar type or not.

def isComplex(array):
    if True in np.iscomplex(array):
        return True
    return False

#reais: naturais, inteiros, racionais, irracionais
def isReal(array):
    if True in np.isreal(array):
        return True
    return False

#scalars: int, float, complex, bool, string
#not scalar: array
def isScalar(array):
    for el in array:
        if np.isscalar(el) == True:
            return True
    return False
array = np.array([[1,1]])

#Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.

def isClose(a, b, tol):
    if False in np.isclose(a, b, atol=tol):
        return False
    return True

#a = np.array([1.0, 2.0, 3.0])
#b = np.array([1.0, 2.3, 2.9])
#tol = 0.2

#Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
#a = np.array([1.0, 2.0, 3.0])
#b = np.array([1.0, 2.3, 2.9])

def greater(a,b):
    return a>b #or np.greater(x,y)

def greater_equal(a,b):
    return a>=b #or np.greater_equal(x,y)

def less(a,b):
    return np.less(a,b)

def less_equal(a,b):
    return np.less_equal(a,b)

#Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.
a = np.array([1, 7, 13, 105])
memory_size = a.nbytes
#print(memory_size)

#Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives. 

array_z = np.zeros(10)
array_o = np.ones(10)
array_c = np.full(10, 5.)

#print(array_c, array_o, array_z)

# Write a NumPy program to create an array of integers from 30 to 70.
x = 30
y = 71
array = np.arange(x, y)
#print("Array de", x, "até", y-1, ":", array)

#Write a NumPy program to create a 3x3 identity matrix.

data = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] # or np.identity(3)
matrix = np.array(data)
#print(matrix)

#Write a NumPy program to generate a random number between 0 and 1.
a = 0
b = 1
random_number = np.random.uniform(a, b)
#print("Random number btw:", a, "e", b, ":", random_number)

#Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.

# standard normal distribution - mean is 0 and standard deviation is 1
# The distribution is symmetrical around the mean.
# The shape of the curve is a bell, which is typical of normal distributions.

#This function generates samples from a snd (Probability Density Function): np.random.randn()

data = np.random.randn(15) #or np.random.normal(0,1,15)

#Write a NumPy program to create a 3X4 array and iterate over it.

a = np.arange(10, 22).reshape((3, 4))

#for el in np.nditer(a):
    #print(el, end = " ")

#Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
val = np.linspace(5, 50, 10)

#Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
v = np.random.randint(0, 21, 20)
#print(v)
def mudar_sinal(v,i1,i2):
    v[i1:i2] = -v[i1:i2]
    return v
#print(mudar_sinal(v,9,16))

#Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
val = np.random.randint(0, 11, 5)

#Write a NumPy program to multiply the values of two given vectors.
a = np.arange(5)
b = np.arange(5)
prod = a * b

#Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
a = np.arange(10, 22).reshape((3, 4))

#Write a NumPy program to find the number of rows and columns in a given matrix.
a = np.arange(10, 22).reshape((3, 4))

#print(len(a),len(a[0])) or
#print("Number of rows and columns of the said matrix:")
#print(a.shape) 
            
#Write a  NumPy program to create a 3x3 identity matrix, i.e. the diagonal elements are 1, the rest are 0.
#i = np.identity(3) or
x = np.eye(3)

