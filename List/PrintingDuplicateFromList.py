# Python code to print the duplicate numbers form a list

def duplicate(list):
    repeated = []
    size = len(list)

    for i in range(size):
        k = i+1
        for j in range(k,size):
            if list[i] == list[j] and lst[i] not in repeated:
                repeated.append(list[i])
    return repeated

lst = [5,7,8,10,21,10,34,-60,10,21,34,-9,7,52,-9]

print("Entered list: ",lst)

print("Duplicate elements in the list:",duplicate(lst))