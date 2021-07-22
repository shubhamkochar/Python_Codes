# Python code to check an item is present in the list

lst = []

num = int(input("Enter the number og elements t add in list: "))

for i in range(0,num):
    elm = int(input("Enter the element: "))
    lst.append(elm)

print("Elements in the list:",lst)

search = int(input("Enter the number to serch in list:"))

if search in lst:
    print(search,"is present in the list.")
else: print(search,"is not present in the list.")


