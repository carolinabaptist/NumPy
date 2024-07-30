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
print(isScalar(array))
