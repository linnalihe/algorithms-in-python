# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573730-921950-1127-6931
# all tests passed
from collections import defaultdict
def four_sum(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # 3 sum looks at each element in arr and looks for the target
    # brute force is to have 4 for loops O(n^4)
    # a for loop to iterate and then another for loop to loop through values on the right
    # for values on the left, create a dictionary
    
    output = []
    seen = set()
    arr.sort()
    
    left_sums = defaultdict(list)
    
    for idx_one in range(1, len(arr)-1):
        for idx_two in range(idx_one+1, len(arr)):
            
            currsum = arr[idx_one] + arr[idx_two]
            
            diff = target - currsum
            
            if diff in left_sums:
                for val in left_sums[diff]:
                    
                    
                    sorted_quad = [val[0], val[1], arr[idx_one], arr[idx_two]]
                    v1, v2, v3, v4 = sorted_quad
                    if not (v1, v2, v3, v4) in seen:
                        
                        output.append([v1, v2, v3, v4])
                        seen.add((v1, v2, v3, v4))

                
        for left_one in range(0, idx_one):
            
            left_sum = arr[left_one] + arr[idx_one]
            sorted_sum = sorted([arr[left_one], arr[idx_one]])
            if not sorted_sum in left_sums[left_sum]:
                left_sums[left_sum].append([arr[left_one], arr[idx_one]])
        

    
    return output