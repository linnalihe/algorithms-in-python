# Q1.5 of Cracking the Coding Interview 6
# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away

inputStr1 = input("First string to compare: ")
inputStr2 = input("Second string to compare: ")


def one_away(input1: str, input2: str):
    diff = len(input1) - len(input2)
    if abs(diff) > 1:
        return False

    diff_index = 0
    if(abs(diff) == 1):
        if(diff == -1):
            shorter = input1
            longer = input2
        else:
            shorter = input2
            longer = input1
        for i in range(len(shorter)):
            if(shorter[i] != longer[i+diff_index]):
                diff_index += 1
    if(diff == 0):
        for i in range(len(input1)):
            if(input1[i] != input2[i]):
                diff_index += 1

    return diff_index <= 1


def sol_one_away(input1: str, input2: str):
    if len(input1) == len(input2):
        return oneEditReplace(input1, input2)
    elif(len(input1) + 1 == len(input2)):
        return oneEditInsert(input1, input2)
    elif(len(input1)-1 == len(input2)):
        return oneEditInsert(input1, input2)
    return False


def oneEditReplace(input1: str, input2: str):
    foundDiff = False
    for idx in range(len(input1)):
        if input1[idx] != input2[idx]:
            if foundDiff:
                return False
            foundDiff = True
    return True


def oneEditInsert(input1: str, input2: str):
    idx1 = 0
    idx2 = 0
    while idx2 < len(input2) and idx1 < len(input1):
        if(input1[idx1] != input2[idx2]):

            if(idx1 != idx2):
                return False
            idx2 += 1
        else:
            idx1 += 1
            idx2 += 1
    return True


def sol2_one_away(input1: str, input2: str):
    if(abs(len(input1) - len(input2)) > 1):
        return False
    # Get shorter and longer string
    s1 = input1 if len(input1) < len(input2) else input2
    s2 = input2 if len(input1) < len(input2) else input1

    idx1 = 0
    idx2 = 0
    foundDiff = False
    while (idx2 < len(input2) and idx1 < len(input1)):
        if(s1[idx1] != s2[idx2]):
            if foundDiff:
                return False
            foundDiff = True
            if(len(s1) == len(s2)):
                idx1 += 1
        else:
            idx1 += 1
        idx2 += 1
    return True


if __name__ == '__main__':
    print(one_away(inputStr1, inputStr2))
    print(sol_one_away(inputStr1, inputStr2))
    print(sol2_one_away(inputStr1, inputStr2))
