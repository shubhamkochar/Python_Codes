# Pyhton code to check whether a sub string is present in a given string

def check(sub_string,string):
    if sub_string in string:
        print("Substring is present in string")
    else:
        print("Substring not found")

check("name is ","Python is a programming language.")