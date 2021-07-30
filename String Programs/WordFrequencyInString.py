# Python code to find the frequency of a word in a string

def frequency(s,w):
    print("Entered string: ",s)
    count = 0
    splited = s.split(" ")
    print(splited)
    size = len(s)
    for x in splited:
        if x == w:
            count +=1
    return count


print("The word is repeated",frequency("You know if you know me","know"),"times.")
