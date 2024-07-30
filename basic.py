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
