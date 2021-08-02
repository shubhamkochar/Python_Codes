# Python code for permutation of given strings using 

from itertools import permutations 

def allpermutation(string):
    permuList = permutations(string)
    for x in list(permuList):
        print("".join(x))


if __name__ == "__main__":
    string = "ABC"
    allpermutation(string)
