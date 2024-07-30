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

a = np.array([[1, 2, 3, 4]])
def isZero(a):
    print(np.all(a))
    return

#Write a NumPy program to test if any of the elements of a given array are non-zero. 
