# Python code to reverse the list items

list = []

num = int(input("Emter the elements to add in the list: "))

for i in range(0,num):
    element = int(input("Enter the element: "))
    list.append(element)

print("List items:",list)

# Creating an empty list to store the reversed list
rev_list = []

# storing the reversed list
rev_list = list[::-1]

print("Reversed list:",rev_list)