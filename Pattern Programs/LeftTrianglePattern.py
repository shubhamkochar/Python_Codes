# Python code to print triangle star pattern

def LeftTriangle(len):
    for i in range(0,len):
        for j in range(0,i+1):
            print("*",end=" ")
        print()


LeftTriangle(5)