#Python code to find negative numbers in a range

start = int(input("Enter the starting range: "))
ending = int(input("Enter the ending range: "))

print("Negative numbers in range from",start,"to",ending,":")

for i in range(start,ending):
    if i <0:
        print(i, end=" ")