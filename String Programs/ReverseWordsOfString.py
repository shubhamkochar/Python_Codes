# Python code to reverse words of a given string

def reverse_str(s):
    print("Original string: ",s)
    splited = s.split(" ")

    reverse = " ".join(reversed(splited))

    print("Reversed string: ",reverse)


reverse_str("Python is a programming language")