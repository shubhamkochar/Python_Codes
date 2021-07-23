# Python code to find the smallest number in the list 

lst = []

num = int(input("Enter the number of elements in the list: "))

for i in range(0,num):
    elm = int(input("Enter the elements: "))
    lst.append(elm)

print("Elements in the list:",lst)

smallest = min(lst)
print("Smallest number in the list is: ",smallest)



