# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573728-917859-1031-6275
# all tests pass
def heap_sort(arr):
    # heapify arr. start with last parent idx
    lastparentidx = (len(arr)-1)//2
    for idx in reversed(range(lastparentidx +1)):
        heapify_down(arr, idx, len(arr)-1)
    
    # loop through backwards to exclude sorted list in decreasing order
    # swap with first index
    for endidx in reversed(range(len(arr))):
        arr[endidx], arr[0] = arr[0], arr[endidx]
        heapify_down(arr, 0, endidx-1)
    
    return arr

# implement heapify_down needed to heapify the arr, and to maintain heap
def heapify_down(arr, curridx, lastidx):
    
    firstchildidx = (curridx*2)+1
    while firstchildidx <= lastidx:
        largeridx = firstchildidx
        secondchildidx = (curridx*2)+2
        if secondchildidx <= lastidx and arr[secondchildidx] > arr[firstchildidx]:
            largeridx = secondchildidx
            
        if arr[curridx] < arr[largeridx]:
            arr[curridx], arr[largeridx] = arr[largeridx], arr[curridx]
        
        curridx = largeridx
        firstchildidx = (curridx*2)+1