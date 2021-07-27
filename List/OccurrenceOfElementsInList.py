# Python code to count the occurrence of elements in a list

def count(list,x):
    count = 0
    for ele in list:
        if ele == x:
            count +=1
    return count

lst = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10]

num = int(input("Enter the number to find the occurrence: "))

print("The number {} is present {} times in the list".format(num,count(lst,num)))