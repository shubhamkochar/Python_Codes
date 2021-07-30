# Python code to print even length of words in a string

def Even_words(s):
    splited = s.split(" ")
    size = len(splited)
    for x in splited:
        if len(x) % 2 == 0:
            print(x)
        

Even_words("Experience is the name everyone gives to their mistakes")