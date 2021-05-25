# Q1.1 of Cracking the Coding Interview 6
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

strInput = input("Check if this string has unique characters: ")


def is_unique(strInput: str) -> bool:
    if(strInput == ""):
        return True

    for i in range(len(strInput)):
        subStr = strInput[i+1:]
        for j in range(len(subStr)):
            if(strInput[i] == subStr[j]):
                return False
    return True

# assuming ascii set
# time O(n), space O(1)


def sol_is_unique(strInput: str) -> bool:
    if len(strInput) > 128:
        return False
    ascii_len = 128
    charset = [None]*ascii_len
    for i in range(len(strInput)):
        ascii_val = ord(strInput[i])
        if(charset[ascii_val]):
            return False
        charset[ascii_val] = True
    return True


def sol2_is_unique(strInput: str) -> bool:
    checker = 0
    for i in range(len(strInput)):
        val = ord(strInput[i]) - ord('a')
        print(val)
        if((checker & (1 << val)) > 0):
            return False

        checker |= (1 << val)

    return True


if __name__ == "__main__":
    print(is_unique(strInput))
    print(sol_is_unique(strInput))
    print(sol2_is_unique(strInput))
