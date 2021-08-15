#Python code for printing square start pattern


def squareStarPattern(side):
    for i in range(0,side):
        for j in range(0,side):
            print("*",end="  ")
        print()

squareStarPattern(5)