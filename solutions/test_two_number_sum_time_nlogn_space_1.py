# ---
# difficulty: easy
# category: array
# name: two number sum time nlogn space 1
# time: O(Nlog(N))
# space: O(1)
# ---
import pytest

def two_number_sum_time_nlogn_space_1(array, targetSum):
    
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left +=1
        elif currentSum > targetSum:
            right -= 1
    
    return []
        



def test_two_number_sum_time_nlogn_space_1():

    array = [3,5,-4,8,11,1,-1,6]
    targetSum = 10

    num_1, num_2 = two_number_sum_time_nlogn_space_1(array, targetSum)

    assert num_1 + num_2  == targetSum