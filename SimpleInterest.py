# Python code to find Simple Interest

def simpleInterest(p,r,t):
    print("\nPrinciple amount: ",p)
    print("Intrest Rate: ",r)
    print("Time Period: ",t)
    si = float((p*r*t)/100)
    return si

# Getting user input 
principle_amount = int(input("Enter the principle amount: "))
interestRate = float(input("Enter the interest rate: "))
timePeriod = int(input("Enter time period in years: "))

# Printing Simple Interest
print("Simple Interest is ",simpleInterest(principle_amount,interestRate,timePeriod))