# Python code to find positive number in a list

lst =[]
num = int(input("Enter the number of elements to insert: "))

for i in range(0, num):
    ele = int(input("Enter both positive and negative number: "))
    lst.append(ele)

print("Entered list is: ",lst)

print("Positive number in list: ")
for x in lst:
    if x>=0:
        print(x,end=" ")