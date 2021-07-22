# Python code to find the length of the list

list = []

num = int(input("Enter the number of elements to add in list: "))

for i in range(0,num):
    element = int(input("Enter the element: "))
    list.append(element)

print("Length of the list is: ", len(list))