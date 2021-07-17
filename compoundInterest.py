# Python code to find Compound Interest

def compoundInterest(p,r,t):
    print("Principle amount: ",p)
    print("Rate :",r)
    print("Time Period: ",t)

    Amount = float(p*(1+r/100) **t)
    return Amount

Principle_Amount = int(input("Enter the principle amount: "))
InterestRate = float(input("Enter Interest rate: "))
TimePeriod = int(input("Enter the time period: "))

print("Compound Interest is ",round(compoundInterest(Principle_Amount,InterestRate,TimePeriod),3))