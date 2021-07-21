# Python code to find the largest element in list

a = []
num = int(input("Enter the number of element to add: "))

for i in range(0,num):
    element = int(input("Enter the element: "))
    a.append(element)

print("Largest element in the list is: ",max(a))
