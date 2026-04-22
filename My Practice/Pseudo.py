#         # #number generation using the random module 

#         # import random
#         # # Generate a random integer between 1 and 10
#         # random_integer = random.randint(1, 10)
#         # print("Random integer between 1 and 10:", random_integer)
#         # # Generate a random floating-point number between 0 and 1
#         # random_float = random.random()
#         # print("Random float between 0 and 1:", random_float)    

#         # #using numerical python to flatten the multidimensional arrays
#         # import numpy as np 
#         # # Create a 2D array
#         # array_2d = np.array([[1, 2, 3], [4, 5, 6]])
#         # print("Original 2D array:")
# # print(array_2d)

# #generating a normal distribution visual using the numpy library
# # set the mean and the standard deviation 
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import random
# mean = 0
# std_dev = 1
# # Generate random numbers from a normal distribution
# # normal_distribution = np.random.normal(mean, std_dev, 1000)
# # #plotting the distributon using the seaborn module 
# # sns.histplot(normal_distribution, #this shows that no histogram is displayed, only the KDE curve
# #              kde=True)
# # plt.title("Normal Distribution")
# # plt.xlabel("Value")
# # plt.ylabel("Frequency")
# # plt.show()
# #using the numpy module to generate a poisson distribution based on random module 
# # set the lambda parameter for the Poisson distribution
# lambda_param = 2

# poisson_distribution = np.random.poisson(lambda_param, 1000)
# sns.histplot(poisson_distribution, kde=True)
# plt.title("Poisson Distribution")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
