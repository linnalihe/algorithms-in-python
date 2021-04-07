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
