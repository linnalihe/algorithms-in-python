# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573731-921952-245-1539
# all tests passed

def pair_sum_sorted_array(numbers, target):
    # bruteforce would be to loop thru and compare each with all the numbers
    # better would be for each number and do binary search O(n log n) time, O(1) space
    # even better is to use 2 pointers and move inwards O(n) time, O(1) space
    left = 0
    right = len(numbers) -1
    
    while left < right:
        currsum = numbers[left] + numbers[right]
        if currsum == target:
            return [left, right]
        
        elif currsum < target:
            left +=1
        else:
            right-=1
    
    return [-1, -1]