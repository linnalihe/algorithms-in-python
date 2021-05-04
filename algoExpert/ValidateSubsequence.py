# Validate Subsequence

# Given two non-empty arrays of integer, find if one is a subsequence of the other.
# Integers do not have ot adjacent to each other but have to be in same order
# Return boolean value

def isValidSubsequence(array, sequence):
    a = 0
    s = 0
    while a < len(array) and s < len(sequence):
        if(array[a] == sequence[s]):
            s += 1
        a += 1

    return s == len(sequence)


def isValidSubsequence(array, sequence):
    s = 0
    for x in array:
        if s == len(sequence):
            break
        if sequence[s] == x:
            s += 1
    return s == len(sequence)
