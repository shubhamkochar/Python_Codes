# Python code to multiply all items in the list

lst = []
num = int(input("Enter the number of elements to insert: "))

for i in range(0,num):
    elm = int(input("Enter the element: "))
    lst.append(elm)

print("Elements in list:",lst)

result =1
for i in lst:
    result = result*i

print("\nMultiplication of elements in the list is:",result)