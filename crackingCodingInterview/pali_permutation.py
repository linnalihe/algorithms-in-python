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


def sol_pali_perm(inputStr: str):
    charFreq = buildCharFrequency(inputStr)
    return checkMaxOneOdd(charFreq)


def checkMaxOneOdd(table: dict):
    foundOdd = False
    for x in table.values():
        if(x % 2 == 1):
            if foundOdd:
                return False
            foundOdd = True
    return True


def buildCharFrequency(phrase: str):
    table = {}
    for char in phrase:
        x = getCharNumber(char)
        if(x != -1):
            table[x] = table.get(x, 0) + 1
    return table


def getCharNumber(letter: str):
    a = ord('a')
    z = ord('z')
    val = ord(letter)
    if(a <= val and val <= z):
        return val - a
    return -1


def sol2_pali_perm(inputStr: str):
    countOdd = 0
    table = [0]*26
    for char in inputStr:
        x = getCharNumber(char)
        if(x != -1):
            table[x] += 1
            if(table[x] % 2 == 1):
                countOdd += 1
            else:
                countOdd -= 1
    return countOdd <= 1


def sol3_pali_perm(inputStr: str):
    bitVector = createBitVector(inputStr)
    return bitVector == 0 or checkExactlyOneBitSet(bitVector)


def createBitVector(inputStr: str):
    bitVector = 0
    for char in inputStr:
        x = getCharNumber(char)
        bitVector = toggle(bitVector, x)
    return bitVector


def toggle(bitVector, idx):
    if idx < 0:
        return bitVector
    mask = 1 << idx

    if((bitVector & mask) == 0):
        bitVector |= mask
    else:
        bitVector &= ~mask
    return bitVector


def checkExactlyOneBitSet(bitVector) -> bool:
    return (bitVector & (bitVector - 1)) == 0


if __name__ == "__main__":
    print(pali_perm(inputStr))
    print(sol_pali_perm(inputStr))
    print(sol2_pali_perm(inputStr))
    print(sol3_pali_perm(inputStr))
