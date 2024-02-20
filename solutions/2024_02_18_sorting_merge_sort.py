# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573728-917859-1031-6267
# all tests passed
def merge_sort(arr):
    # call a merge helper
    # helper will sort the two halves and then combine them
    sorted_arr = merge_helper(arr, 0, len(arr)-1)
    return sorted_arr
    
def merge_helper(arr, start, end):
    
    if start >= end:
        return [arr[end]]
    
    mid = (start+end)//2
    left_side = merge_helper(arr, start, mid)
    right_side = merge_helper(arr, mid+1, end)
    
    left = 0
    right = 0
    temp = []
    while left < len(left_side) and right < len(right_side):
        if left_side[left] < right_side[right]:
            temp.append(left_side[left])
            left+=1
        else:
            temp.append(right_side[right])
            right+=1
            
    while left < len(left_side):
        temp.append(left_side[left])
        left+=1
        
    while right < len(right_side):
        temp.append(right_side[right])
        right+=1
        
        
    return temp