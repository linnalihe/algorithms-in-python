# Validate Subsequence

# Given two non-empty arrays of integer, find if one is a subsequence of the other.
# Integers do not have ot adjacent to each other but have to be in same order
# Return boolean value

# iterate sequence, increment pointer if value in array in same order
# return true if pointer for sequence is length of sequence
def isValidSubsequence(array, sequence):
    sPointer = 0
    aPointer = 0
    while sPointer < len(sequence) and aPointer < len(array):
        if(array[aPointer] == sequence[sPointer]):
            sPointer += 1
            aPointer += 1
        else:
            aPointer += 1
    return sPointer == len(sequence)
