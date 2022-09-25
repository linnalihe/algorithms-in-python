# ---
# difficulty: easy
# category: array
# name: two number sum time N^2 space 1
# time: O(N^2)
# space: O(1)
# ---
import pytest

def two_number_sum_time_n2_space_1(array, targetSum):
    #code here
    for num_1 in array:
        for num_2 in array:
            if num_1 != num_2 and num_1 + num_2 == targetSum:
                return [num_1, num_2]

    return []


def test_two_number_sum_time_n2_space_1():

    array = [3,5,-4,8,11,1,-1,6]
    targetSum = 10

    num_1, num_2 = two_number_sum_time_n2_space_1(array, targetSum)

    assert num_1 + num_2  == targetSum
