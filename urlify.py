# Q1.3 of Cracking the Coding Interview 6

strInput = input("Give me a sentence with spaces: ")
spaceCount = 0
for char in strInput:
    if char == " ":
        spaceCount += 1

strLen = len(strInput) + 2*spaceCount


def urlify(strInput: list, strLen: int) -> str:
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


print(urlify(list(strInput), strLen))
