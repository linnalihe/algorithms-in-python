# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573730-921950-1127-6899
# all tests passed
def find_zero_sum(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    # brute force is to comapre all numbers with time O(n^3) and space O(n) for output
    # arr may contain duplicates
    # sort and then have a for loop iterate through and find the target 
    # in the remaining left side of the array
    # time is O(n^2), space is O(n) for the output
    
    output = set()
    arr.sort()
    
    for idx in range(len(arr)):
        target = 0 - arr[idx]
        left = idx +1
        right = len(arr) -1
        while left < right:
            currsum = arr[left] + arr[right]
            if currsum == target:
                output.add(f"{arr[idx]}, {arr[left]}, {arr[right]}")
                left+=1
                right-=1
            elif currsum < target:
                left+=1
            elif currsum > target:
                right-=1
                
    return list(output)