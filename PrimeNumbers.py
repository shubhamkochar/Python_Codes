# Python code to find whether a number is prime or not

def primeNumber(n):
    print("Number entered is: ",n)

    if (n<=1):
        print("Nither Prime nor composite")

    for i in range(2,n):
        if (n % i ==0):
           print("Not Prime")
           
        else:
            print("Prime")
        break

num = int(input("Enter the number to check: "))
primeNumber(num)

