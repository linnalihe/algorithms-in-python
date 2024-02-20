# all tests passed
def heap_sort(arr):
    # heapify the array
    # swap the last with the first and contract the array to exclude the last
    # move the largest element down to the right place
    
    # heapify
    for lastparentidx in reversed(range(((len(arr)-1)//2) + 1)):
        heapify_down(arr, lastparentidx, len(arr)-1)
    
    # in place sort using heap
    for lastidx in reversed(range(len(arr))):
        arr[lastidx], arr[0] = arr[0], arr[lastidx]
        heapify_down(arr, 0, lastidx-1)
    
    return arr

def heapify_down(arr, curridx, endidx):
    
    firstcidx = curridx*2 +1
    while firstcidx <= endidx:
        
        # pick larger child
        largeridx = firstcidx
        secondcidx = curridx*2+2
        if secondcidx <= endidx and arr[secondcidx] > arr[firstcidx]:
            largeridx = secondcidx
            
        if arr[curridx] < arr[largeridx]:
            arr[curridx], arr[largeridx] = arr[largeridx], arr[curridx]
        
        curridx = largeridx
        firstcidx = curridx*2 +1