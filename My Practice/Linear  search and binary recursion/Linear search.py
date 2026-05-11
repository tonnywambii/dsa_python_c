import random
#defining the linear search function
def linear_search (values, target):
    for i in range (len(values)):
        if values[i] == target:
            return i
    return -1

def get_values ():
    values = list(random.sample(range(1, 101), k=5))
    print (f"The list is : {values}")
    target = int(input("Enter the target value: "))
    result = linear_search(values, target)
    if result < 0:
        print("Target not found")
    else:
        print(f"Target found at index: {result}")
get_values()
        
        