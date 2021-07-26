# Python code to print negative numbers in a list

lst = []
num = int(input("Enter the number of elements to insert: "))

for i in range(0,num):
    ele = int(input("Enter both negative and positive numbers: "))
    lst.append(ele)

print("Entered list: ",lst)


print("Negative number in list: ")
for x in lst:
    if x<0:
        print(x,end=" ")

