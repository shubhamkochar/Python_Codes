# Python code to get the words greater than the given length 

def greater_words(string,num):
    splited = string.split(" ")
    words = []
    for x in splited:
        if len(x)>num:
            words.append(x)
        else:
            pass
    print(words)

if __name__ == "__main__":

    sentence = "Earlier versions of Python did not attempt to create instances of the derived class"

    num = int(input("Enter the length: "))

    print("Words greater than the length of",num,"in string: ")

    greater_words(sentence,num)
