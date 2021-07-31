# Python code to remove all duplicates from a string

def removeDuplicate(string):
    print("Original String: ",string)
    r =""
    for i in string:
        if (i in r):
            pass
        else:
            r = r+i
    print("String after removing duplicates: ",r)



removeDuplicate("repetition")