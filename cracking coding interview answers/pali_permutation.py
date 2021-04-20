# Q1.4 of Cracking the Coding Interview 6
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

inputStr = input("Check if this string is a palindrome permutation: ")


def pali_perm(inputStr: str):
    inputStr = inputStr.strip(" ")
    strDict = {}
    for x in inputStr:
        strDict[x] = strDict.get(x, 0) + 1
    count_solo = 0
    for val in strDict.values():
        if val % 2 != 0:
            count_solo += 1
    if count_solo > 1:
        return False
    else:
        return True


print(pali_perm(inputStr))
