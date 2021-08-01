# Python code to find uncommon words in two string

def uncommon_words(string1,string2):
    print("\nString 1: ",string1)
    print("\nString 2:",string2)

    splited1 = string1.split(" ")
    splited2 = string2.split(" ")

    uncommon = []

    for i in splited1:
        if i not in splited2:
            uncommon.append(i)

    for j in splited2:
        if j not in splited1:
            uncommon.append(j)
    
    return uncommon


if __name__ == "__main__":

    string1 = "I live in New Jersey"
    string2 = "I live in London"
    print("Uncommon words: ",uncommon_words(string1,string2))
