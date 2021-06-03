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


def replace_spaces(strInput: list, strLen: int) -> str:

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


def sol_replace_spaces(strInput: list, strLen: int) -> str:

    index = 0
    strOutput = [None]*strLen
    index = strLen
    for i in range(len(strInput)-1, -1, -1):
        if(strInput[i] == " "):
            strOutput[index - 1] = "0"
            strOutput[index - 2] = "2"
            strOutput[index - 3] = "%"
            index = index - 3
        else:
            strOutput[index - 1] = strInput[i]
            index -= 1
    return "".join(str(c) for c in strOutput)


if __name__ == "__main__":
    print(replace_spaces(list(strInput), strLen))
    print(sol_replace_spaces(list(strInput), strLen))
