# AlgoExpert
# String, Easy
# Given lowercase english alphabet, return index of first non-repeating character

def firstNonRepeatingCharacter(string):
    # Write your code here.
    letterTable = {}
    for ch in string:
        letterTable[ch] = letterTable.get(ch, 0)+1

    for i, ch in enumerate(string):
        if letterTable[ch] == 1:
            return i
    return -1


# first non repeating
# keep track of count in a hashmap?
# iterate through the string again
