# Python code to find factorial of number

def factorial(n):
    if n <0:
        return "Factorial is 0"
    elif n ==0 or n==1:
        return "Factorial is 1"
    else:
        fact = 1
        while(n>1):
            fact *= n
            n -=1
        return fact

num = int(input("Enter the number to find the factorial: "))
print("Factorial of ",num,"is ",factorial(num))
