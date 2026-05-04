numbers =[1,2,3,4,5,6,7,8,9,10]
print("Original list: ", numbers)#s
#comparison as a basis for searching and sorting algorithms
for i in range(len(numbers)):
    if numbers[i] < numbers[i-1]: #comparing the current element with the previous one
        print("Found 5 at index:", i)
        break
#for linked lists pointing to the next node is a must to ensure continuity
#for linked lists any addition to the memory ,it does not affect the original list since they are not stored in contiguous memory locations like arrays.
#Check for time and space complexity brought about by the changes to the array 
#building a stack and a queue using pop and append methods 
#pick :used to select the element at the top 
