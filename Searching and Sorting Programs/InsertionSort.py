# Python code for insertion sort

import time 

def InsertionSort(arr):
    print("Unsorted array: ",arr)
    size = int(len(arr))

    for i in range(1,size):
        k = arr[i]
        j =i-1
        while j>=0 and k<arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = k 


if __name__ == "__main__":
    start_time = time.time()
    arr= [21,4,9,31,74,65,89,41]
    InsertionSort(arr)

    print("Sorted array:",arr)

    end_time = time.time()
    print(f"Runtime of program is {end_time - start_time}")