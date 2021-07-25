# Python code to print odd numbers in a list

lst = []

num = int(input("Enter the number of elements in list: "))

for i in range(0,num):
    ele = int(input("Enter the element: "))
    lst.append(ele)

print("Elements in list: ",lst)

print("Odd numbers in list: ")
for x in lst:
    if(x%2 != 0):
        print(x,end=" ")


