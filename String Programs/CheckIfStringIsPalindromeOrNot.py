# Python code to check whether a string is palindrom or not 

def palindrome(s):
    if s == s[::-1]:
        print("String is palindrome.")
    else:
        return print("String is not palindrome.")

palindrome("noon")