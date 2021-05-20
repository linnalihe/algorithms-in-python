
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
