def isPalindrome(string):

    idx1 = 0
    idx2 = len(string)-1

    return isPalindromeHelp(string, idx1, idx2)


def isPalindromeHelp(string, idx1, idx2):
    if idx1 == idx2 or idx1+1 == idx2:
        return string[idx1] == string[idx2]

    return string[idx1] == string[idx2] and isPalindromeHelp(string, idx1+1, idx2-1)

    # when using recursion:
    # each time you call isPalindrome the string shrinks
    # once you get to string length is 1 or string length is 2:
    # return if value at idx1 is same as idx2


def isPalindrome2(string):
    start = 0
    end = len(string)-1

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True
