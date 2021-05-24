# Q1.3 of Cracking the Coding Interview 6
# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith
# Output: "Mr%20J ohn%20Smith"

strInput = input("Give me a sentence with spaces: ")
spaceCount = 0
for char in strInput:
    if char == " ":
        spaceCount += 1

strLen = len(strInput) + 2*spaceCount


def replaceSpaces(strInput: list, strLen: int) -> str:

    strOutput = [None]*strLen

    offset = 0
    for i in range(len(strInput)):
        if(strInput[i] == " "):
            strOutput[i+offset] = "2"
            strOutput[i+offset+1] = "0"
            strOutput[i+offset+2] = "%"
            offset += 2
        else:

            strOutput[i+offset] = strInput[i]

    return "".join(str(char) for char in strOutput)


def replaceSpaces2(strInput: list, strLen: int) -> str:
    spaceCount = 0
    index = 0
    i = 0
    strOutput = [None]*strLen
    for i in range(len(strInput)):
        if(strInput[i] == " "):
            spaceCount += 1

    index = strLen + spaceCount*2
    for i in range(strLen-1, -1, -1):
        print(i)
    return "".join(str(c) for c in strOutput)


if __name__ == "__main__":
    print(replaceSpaces(list(strInput), strLen))
    print(replaceSpaces2(list(strInput), strLen))
