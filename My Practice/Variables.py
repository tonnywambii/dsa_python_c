# print("Hello, World!")

# name = "Brian"
# num= 25 
# balance = 100.50
# flag= True

# print("Name''s type :", type(name))
# print("Number''s type :", type(num))
# print("Balance''s type :", type(balance))
# print("Flag''s type :", type(flag))

# #loops and functions 
# for i in range(5):
#     print("Iteration:", i)
#pointing to the same memory location 
a = [1, 2, 3]
b = a
print("a:", a)
print("b:", b)
#modifying b will also modify a since they point to the same list
b.append(4)
print("After modifying b:")
print("a:", a)

#multiline comments (used for python documentation)
multiline_string = """This is a multiline string.
It can span multiple lines. """
print(multiline_string)

