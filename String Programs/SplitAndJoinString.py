# Pyhton code to split and join a string

def main(s):
    print("\nOriginal string: ",s)
    splited = s.split(" ")
    print("\nSplited string: ",splited)
    joined = "-".join(splited)
    print("\nJoined string",joined)



if __name__ == "__main__":
    main("To search the internet for Python related topics, use Python Search")