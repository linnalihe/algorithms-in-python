# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573730-921950-1127-6911
# all tests passed
def count_triplets(target, numbers):
    """
    Args:
     target(int32)
     numbers(list_int32)
    Returns:
     int32
    """
    # brute force is to create all triplets and compare it to target
    # time O(n^3)
    # better to do the same as 3 sum but add if triplet is smaller
    # time: O(n^2), space: O(1)
    
    numbers.sort()
    
    count = 0
    for idx in range(len(numbers)):
        start = idx+1
        end = len(numbers) -1
        while start <= end:
            currsum = numbers[idx] + numbers[start] + numbers[end]
            if currsum < target:
                # Crux
                # if currsum < target it means that the start + all numbers to it's right will
                # result in currsum < target
                count+= end-start
                start+=1
            else:
                end-= 1
    
    return count