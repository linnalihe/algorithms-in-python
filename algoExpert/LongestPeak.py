
# Given array of integers, return the length of longest peak;
# peaks are numbers where the number to the left is smaller and the number to the right is smaller
# If the number to either the right or the left are same as the number, it is not a peak (1,2,1 where 2 is a peak), (1,2,2,1, where 2 is not a peak)
# At least 3 integers are required for a peak

def longestPeak(array):
    longest = 0
    for i in range(1, len(array)-1):
        # check that number on left and number on right are both smaller
        if(array[i-1] < array[i] and array[i+1] < array[i]):
            # counter is set to 3 because that is length of peak at this point
            # go left and add to counter as long as next left is smaller
            # go right and add to counter as long as next right is smaller
            counter = 3
            left = i-1
            while left-1 >= 0 and array[left-1] < array[left]:
                counter += 1
                left -= 1
            right = i+1
            while right+1 < len(array) and array[right+1] < array[right]:
                counter += 1
                right += 1

            if counter > longest:
                longest = counter

    return longest

# iterate though all the items in an array
# longestpeak to track longest
# peakcount to count length of peak
# if increasing, increment counter
# if decreasing, increment counter
# only compare templen to longestpeak when there is a +1 (increment) and -1 (decrement) and
# +1 increment again or end of array

# more complicated approach compared to finding peaks first, (incomplete)


def longestPeak2(array):
    longestpeak = 0
    idx = 0
    while idx < len(array):
        pass
    # check if val is increasing
        # scenerios:
        # have been increasing
        # have been decreasing
        # already increase and decreased
        # check if val is decreasing
        # scenerios:
        # have been increasing
        # if value is staying the same
        # zero out the peakcount
    return longestpeak
