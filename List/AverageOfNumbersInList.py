# Python code to find the average of numbers in a given list

# defining an empty array
a =[]

n = int(input("Enter the number of values to add in list: "))


for i in range(0,n):
    num = int(input("Enter the element in array: "))
    a.append(num)

# finding average 
avg = sum(a)/n
print("Average of elements inthe list", round(avg,2))

