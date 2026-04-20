#number generation using the random module 

import random
# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print("Random integer between 1 and 10:", random_integer)
# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random float between 0 and 1:", random_float)    

#using numerical python to flatten the multidimensional arrays
import numpy as np 
# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])