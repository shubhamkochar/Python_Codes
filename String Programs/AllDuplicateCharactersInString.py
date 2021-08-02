# Python code to find the all duplicate characters in a string

def duplicate(s):
    print("Entered string: ",s)
    size = len(s)
    dupli_char = []
    for i in range(size):
        for j in range(i+1,size):
            if s[i] == s[j]:
                dupli_char.append(s[i])
            else:
                pass
    print("Duplicate characters:",dupli_char)


duplicate("Imagination")
