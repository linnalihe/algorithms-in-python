# Monotonic Array
# Given array of integers return True if continuously increasing or continuously decreasing
#                         return False if not continuous

# if increasing, current  > previous
# if decreasing, current  < previous
# if static, current  == previous
def isMonotonic(array):
    if array == [] or len(array) <= 2:
        return True
# [1, 3] 3-1 = +2
# [3, 1] 1-3 = -2
# [-5,3] 3--5 = 8
# [2, -1] -1 - 2 = -3
    direction = array[1] - array[0]

    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i-1]
        # increasing
        if direction > 0 and array[i-1] > array[i]:
            return False
        # decreasing
        elif direction < 0 and array[i-1] < array[i]:
            return False

    return True
