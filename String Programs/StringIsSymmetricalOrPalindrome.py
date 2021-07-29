# Python code to check whether a string is Symmetrical or Palindrome

def symmetrical(s):
    size = len(s)
    print("Length: ",size)
    mid = int(size/2)
    k = mid
    for i in range(0,mid):
        if s[i] == s[k]:
            k +=1
        else: 
            print("False")
            break
        print("True")
        break


symmetrical("khokpo")