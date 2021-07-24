# Python code to find the second largest number in the list

lst =[]

num = int(input("Enter the number of elements to insert: "))

for i in range(0,num):
    ele = int(input("Enter the element: "))
    lst.append(ele)

print("Elements of list: ",lst)
print("Second largest element in the list is: ",sorted(lst)[-2])