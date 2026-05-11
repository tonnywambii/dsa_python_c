import random 
def binary_recursion (values, target, low, high):
    if low  < high:
        return -1
    mid = (low + high) // 2
    
    #best case scenario
    if values[mid] == target:
        return mid
    elif values[mid] > target:
        return binary_recursion(values, target, low, mid-1)
    else:
        return binary_recursion(values, target, mid+1, high)
    return -1

def get_values ():
    values = list(random.sample(range(1, 101), k=5))
    print (f"The list is : {values}")
    target = int(input("Enter the target value: "))
    result = binary_recursion(values, target, 0, len(values)-1)
    if result == -1:
        print("Target not found")
    else:
        print(f"Target found at index: {result}")
get_values()
        
        