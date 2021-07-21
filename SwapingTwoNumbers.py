# Python code to swap two numbers with using third variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# printing values before swaping
print("First number is",num1,"and second number is",num2)

# swaping values 
num1,num2 = num2,num1

# printing values after swaping
print("After Swaping,\nFirst number is",num1,"and second number is",num2)
