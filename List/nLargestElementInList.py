# Python code to find N largest element in the list

lst = []

num = int(input("Enter the number of elements to insert: "))

for i in range(0,num):
    ele = int(input("Enter the element: "))
    lst.append(ele)

print("Elements in the list: ",lst)

N = int(input("Enter the N largest element to find: "))
print(N,"largest number in the list is: ",sorted(lst)[-N])