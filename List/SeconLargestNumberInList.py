# Python code to find the second largest number in the list

lst = [24,74,36,47,65,92,94,61]

largest = max(lst)
smallest = min(lst)

# for i in range(len(lst)):
#     if largest<lst[i]:
#         print("Second largest number is:",lst[i])
#     else:

print(max(lst[0],lst[1]))