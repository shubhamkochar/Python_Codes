# Python code for binary search with runtime in milliseconds
import time 

def BinarySearch(arr,num):
    print("Array: ",arr)
    beg = 0
    end = int(len(arr))

    while beg<=end:
        mid = int((beg+end)/2)
        if num == arr[mid]:
            return mid 
        elif num > arr[mid]:
            beg = mid +1
        else:
            end = mid -1
    return -1

if __name__ == "__main__":
    start = time.time()

    arr =[2,4,7,9,11,13,14,18,21,23,28,32]
    num = int(input("Enter the number to search: "))
    ans = BinarySearch(arr,num)

    if ans == -1:
        print("Not found")
    else:
        print("Number",num,"found at index:",ans)


    end_time = time.time()
    print(f"Runtime of program is {end_time-start}")