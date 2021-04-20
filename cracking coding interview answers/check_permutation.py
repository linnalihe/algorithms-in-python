# Q1.2 of Cracking the Coding Interview 6
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

strInput1 = input("give me the first string: ")
strInput2 = input("give me the second string: ")


def check_perm(input1: str, input2: str):

    strDict = {}

    for x in input1:
        strDict[x] = True
    for y in input2:
        if not strDict.get(y, False):
            return False
    return True


print(check_perm(strInput1, strInput2))
