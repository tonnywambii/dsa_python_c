def a(n):
    # if n > 0:
    #     print(f"Inside a: {n}")
    #     return n
    #this two codes will work the same but the first one is more efficient since it will not make the recursive call if n is greater than 0
    if n < 1:
        return n 
    else:
        print(f"Inside a: {n}")
        return b(n-1)
def b(n):
    if n > 0:
        print(f"Inside b: {n}")
        return n
    return a(n-1)
b(5)