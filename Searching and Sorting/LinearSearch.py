# Python code for Linear search with runtime in milliseconds
import time

def LinearSearch(arr,num):
    print("Entered array: ",arr)
    size = int(len(arr))
    
    for i in range(0,size):
        if (arr[i] == num):
            return i
    return -1

if __name__ == "__main__":
    start_time = time.time()

    arr =[2,4,7,9,11,13,14,18,21,23,28,32]
    num = int(input("Enter the number to search: "))
    ans = LinearSearch(arr,num)

    if ans != -1:
        print("Number",num,"found at index: ",ans)
    else:
        print("Not found")
    
    end_time = time.time()

    print(f"Runtime of program is {end_time-start_time}")