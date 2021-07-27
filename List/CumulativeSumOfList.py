# Python code to print the cumulative sum of a list

def CumulativeSum(list):
    size = len(list)
    new_list = []
    j=0
    for i in range(size):
        j += list[i]
        new_list.append(j)
    return new_list

lst = [1,10,20,30,40,50]
print("Cumulative sum of list:", CumulativeSum(lst))
