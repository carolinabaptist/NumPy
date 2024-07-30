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
