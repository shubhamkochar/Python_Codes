#Python code for rectangle star pattern 

def rectanglePattern(l,b):
    for i in range(0,l):
        for j in range(0,b):
            print("*",end=" ")
        print()

rectanglePattern(5,3)