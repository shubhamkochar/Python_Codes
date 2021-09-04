#Python code for Bubble sort 

import time 

def BubbleSort(lst):
    size = int(len(lst))
    for i in range (0,size):
        for j in range (i+1,size):
            if lst[j]<lst[i]:
                lst[i],lst[j] = lst[j],lst[i]

if __name__ == "__main__":
    start_time = time.time()
    lst = [4,5,74,65,12,87,63,98,25,76]
    print("Before sorting: ",lst)
    BubbleSort(lst)
    print("After sorting:",lst)

    end_time= time.time()
    print(f"Runtime of program:{end_time-start_time}")