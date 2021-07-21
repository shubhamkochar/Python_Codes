# Python code to compute the sum of n+nn+nnn

def sum(n):
    sum =0
    for i in range(1,n+1):
        sum = sum+(n**i)
        i+=1
    return sum

num = int(input("Enter the number: "))
print("Sum of series n+nn+nnn is :",sum(num))