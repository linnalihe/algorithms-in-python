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


# def str_compress(inputStr: str):
#     currStr = inputStr[0]
#     count = 0
#     newStr = ""
#     for i in range(len(inputStr)):

#         if currStr is not inputStr[i]:
#             newStr += currStr+str(count) if count > 1 else currStr
#             currStr = inputStr[i]
#             count = 1
#             if i == len(inputStr)-1:
#                 newStr += currStr+str(count) if count > 1 else currStr

#         else:
#             count += 1
#             if i == len(inputStr)-1:
#                 newStr += currStr+str(count) if count > 1 else currStr

#     return newStr


if __name__ == "__main__":
    print(str_compress(inputStr))
