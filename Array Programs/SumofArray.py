# Python code to find the sum of array 

def sumOdArray(arr):
    sum = 0
    for i in arr:
        sum = sum +i
    
    return sum

# defining an empty array
arr=[]

# storing values in the empty array
arr = [12,3,8,75]

# storing array sum in ans variable
ans = sumOdArray(arr)

# printing sum of array
print("Sum of array is: ",ans)