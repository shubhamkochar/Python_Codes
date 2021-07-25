# Python code to find the even numbers in a list

lst = []

num = int(input("Enter the numbers of elements to insert: "))

for i in range(0,num):
    ele = int(input("Enter element number: "))
    lst.append(ele)

print("Elements in list: ",lst)

print("Even numbers in list: ")
for x in lst:
    
    if(x%2 == 0):
        print(x,end=" ")

