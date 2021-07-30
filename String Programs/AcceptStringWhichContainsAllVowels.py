# Python code to accept string which contains all vowels


def check(string):
    string = string.lower()

    vowels = set("aeiou")

    s = set({})

    for x in string:
        if x in vowels:
            s.add(x)
        else:
            pass

    
    if len(s) == len(vowels):
        print("String accepted!")
    else:
        print("String not accepted!")

if __name__ == "__main__":

    string1 = "Realistic"
    string2 = "geaeyiforcu"

    check(string1)
    check(string2)




