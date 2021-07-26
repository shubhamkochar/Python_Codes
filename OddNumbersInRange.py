# Python code to find odd numbers in a range

start = int(input("Enter the starting range to find even numbers: "))
end = int(input("Enter the end range: "))

print("Odd numbers in range from",start,"to",end,":")
for x in range(start,end+1):
    if (x%2 !=0):
        print(x,end=" ")


