# ---
# difficulty: easy
# category: array
# name: two number sum time N space N
# time: O(N)
# space: O(N)
# ---

import pytest

def two_num_sum_time_n_space_n(array, targetSum):
    diff_lookup = {}
    for n in array:
        diff = targetSum - n
        if diff in diff_lookup:
            return [diff, n]
        diff_lookup[n] = True
    return []



def test_two_num_sum_time_n_space_n():

    array = [3,5,-4,8,11,1,-1,6]
    targetSum = 10
    num_1, num_2 = two_num_sum_time_n_space_n(array, targetSum)

    assert num_1 + num_2 == targetSum