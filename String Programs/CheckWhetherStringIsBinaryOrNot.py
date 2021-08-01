# Python code to check whether a string is binary string or not 

def check(s):
    t = set(s)
    b = {"0","1"}

    if b == t or t == {"0"} or t == {"1"}:
        print("String accepted:",s)
    else:
        print("String not accepted:",s)



if __name__ == "__main__":
    check("110010101101")
    check("11012110102100")