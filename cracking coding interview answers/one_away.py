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


if __name__ == '__main__':
    print(one_away(inputStr1, inputStr2))
