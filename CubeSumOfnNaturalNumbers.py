# Python code to find the cube sum of first n natural number

def sum(n):
    sum =0
    for i in range(n+1):
        sum = sum + (i**3)
    return sum

num = int(input("Enter the number: "))
print("Sum of cube of",num,"natural number is",sum(num))