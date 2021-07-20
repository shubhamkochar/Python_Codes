# Python code to find the sum of square of n natural numbers

def Sum(n):
    sum =0
    for i in range(n+1):
        sum = sum + (i**2)
    return sum
    
num = int(input("Enter a natural number: "))
print("Sum of square of",num,"natural number is:",Sum(num))