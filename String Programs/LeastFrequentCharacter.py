# Python code to find the least frequent character from a string

def least_frequent(s):
    print("Entered string: ",s)
    frequency ={}
    for i in s:
        if i in frequency:
            frequency[i] +=1
        else:
            frequency[i]= 1

    result = min(frequency)
    print("Minimum of all character in string: ",result)

least_frequent("Pneumonoultramicroscopicsilicovolcanoconiosis")