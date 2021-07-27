# Python code to remove unwanted elements form a list(here we are removing even numbers).

# Creating a empty list
lst =[]

# Taking number of inputs 
num = int(input("Enter the number of elements to insert in list: "))

# Taking user inputs 
for i in range(0,num):
    ele= int(input("Enter the number:"))
    lst.append(ele)

# Printing entered list
print("Entered list: ",lst)

# Removing unwanted elements form list
for x in lst:
    if x % 2 == 0:
        lst.remove(x)

# Printing new list
print("New list after removing even numbers: ",lst)