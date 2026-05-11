def tail_recursion (n):
    if n < 0:
        return n
    print(n)
    return tail_recursion(n-1) + tail_recursion(n-1)
tail_recursion(5)#tail recursion since the recursive call is the last thing executed