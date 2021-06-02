# Q1.6 of Cracking the Coding Interview 6
# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

inputStr = input("Compress string: ")


def str_compress(inputStr: str):
    strDict = {}
    newStr = ""
    for char in inputStr:
        strDict[char] = strDict.get(char, 0)+1
    for key, val in strDict.items():
        if val > 1:
            newStr += key+str(val)
        else:
            newStr += key

    return newStr


def sol_str_compress(inputStr: str):
    compressedStr = ""
    countConsec = 0
    for i in range(len(inputStr)):
        countConsec += 1
        if(i+1 >= len(inputStr) or inputStr[i] != inputStr[i+1]):
            compressedStr += inputStr[i] + str(countConsec)
            countConsec = 0
    return compressedStr if len(compressedStr) < len(inputStr) else inputStr


def sol2_str_compress(inputStr: str):
    finalLen = countCompression(inputStr)
    if(finalLen >= len(inputStr)):
        return inputStr
    compressedStr = ""
    countConsec = 0
    for i in range(len(inputStr)):
        countConsec += 1
        if(i+1 >= len(inputStr) or inputStr[i] != inputStr[i+1]):
            compressedStr += inputStr[i] + str(countConsec)
            countConsec = 0
    return compressedStr if len(compressedStr) < len(inputStr) else inputStr


def countCompression(inputStr: str):
    compressedLen = 0
    countConsec = 0
    for i in range(len(inputStr)):
        countConsec += 1

        if(i+1 >= len(inputStr) or inputStr[i] != inputStr[i+1]):
            compressedLen += 1
            countConsec = 0
    return compressedLen


if __name__ == "__main__":
    print(str_compress(inputStr))
    print(sol_str_compress(inputStr))
    print(sol2_str_compress(inputStr))
