# Python code to check whether a string is Symmetrical or Palindrome

def symmetrical(s):
    size = len(s)
    flag = 0
    if size %2:
        mid = size//2 +1
    else:
        mid = size//2
    
    start1 =0
    start2 =mid 

    while(start1 < mid and start2 < size):
        if(s[start1] == s[start2]):
            start1 +=1
            start2 +=1
        else:
            flag = 1
            break

    if flag == 0:
        print("Entered string is symmetrical")
    else:
        print("Entered string is not symmetrical")

def palindrome(s):
    if s == s[::-1]:
        print("Entered string is palindrome")
    else:
        print("Entered string is not plaindrome")

symm = str(input("Enter string to check its symmetricity: "))
palin = str(input("Enter string to check palindrome: "))

symmetrical(symm)
palindrome(palin)