# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573728-917859-1031-6270
# all tests passed

import random
def quick_sort(arr):

    quick_sort_helper(arr, 0, len(arr)-1)
    return arr
    
    
def quick_sort_helper(arr, start, end):
    
    if start >= end:
        return
    
    pivot = random.randint(start, end)
    arr[pivot], arr[start] = arr[start], arr[pivot]
    
    smaller = start
    larger = smaller+1
    while larger <= end:
        if arr[larger] < arr[start]:
            smaller+=1
            arr[smaller], arr[larger] = arr[larger], arr[smaller]
            
        larger+=1
    arr[start], arr[smaller] = arr[smaller], arr[start]
    
    
    quick_sort_helper(arr, start, smaller-1)
    quick_sort_helper(arr, smaller+1, end)