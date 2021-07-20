# Python code to write the fibonacci series

def fibonacci(n):
    t1 = 0
    t2 =1
    nextTerm = t1+t2
    for i in range(3,n):
        print(nextTerm)
        t1 = t2
        t2 = nextTerm
        nextTerm = t1 + t2

num = int(input("Enter the number of series: "))

print(fibonacci(num))