# Q1.2 of Cracking the Coding Interview 6
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

strInput1 = input("give me the first string: ")
strInput2 = input("give me the second string: ")


def check_perm(input1: str, input2: str):

    if len(input1) != len(input2):
        return False
    strDict = {}

    for x in input1:
        strDict[x] = strDict.get(x, 0) + 1
    for y in input2:
        strDict[y] = strDict.get(y, 0) - 1
        if strDict[y] < 0:
            return False
    return True


def sort_string(inputStr: str) -> str:
    strArr = [char for char in inputStr]
    strArr.sort()
    return "".join(strArr)

# sorting the array and then comparing the sorted string


def check_perm2(input1: str, input2: str):
    if len(input1) != len(input2):
        return False
    return sort_string(input1) == sort_string(input2)

# create a 128 len array and count characters, compare array


def check_perm3(input1: str, input2: str) -> str:
    if len(input1) != len(input2):
        return False

    letters = [0]*128
    for char in input1:
        letters[ord(char)] += 1
    for char in input2:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False
    return True


if __name__ == "__main__":
    print(check_perm(strInput1, strInput2))
    print(check_perm2(strInput1, strInput2))
    print(check_perm3(strInput1, strInput2))
