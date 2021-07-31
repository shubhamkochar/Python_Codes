# Python code to find the maximum character in string

def Maximum_char(s):
    frequency ={}
    for i in s:
        if i in frequency:
            frequency[i] +=1
        else:
            frequency[i] = 1

    result = max(frequency, key = frequency.get)
    return result

print("Maximum character: " +str(Maximum_char("Pneumonoultramicroscopicsilicovolcanoconiosis")))
