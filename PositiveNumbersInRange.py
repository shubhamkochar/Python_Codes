#Python code to find positive numbers in a range

start = int(input("Enter the starting range: "))
ending = int(input("Enter the ending range: "))

print("Postive numbers in range from",start,"to",ending,":")
for i in range(start,ending):
    if i >=0:
        print(i, end=" ")