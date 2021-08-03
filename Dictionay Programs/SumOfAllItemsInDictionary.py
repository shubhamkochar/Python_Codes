# Python code to find sum of all items in dictionary

def sum(d):
    print("Entered dictionary: ",d)
    sum =0
    for x in d.values():
        sum = sum +x
    return sum


dictionary = {"a":100,"b":45,"c":78,"d":98}
print("Sum: ",sum(dictionary))
