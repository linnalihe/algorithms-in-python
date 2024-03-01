# https://leetcode.com/problems/word-break/description/
# all tests passed
def wordBreak(s: str, wordDict: list[str]) -> bool:
    # chop the word and pass the remaining segment to check if it's in dictionary

    # if s in wordDict:
    #     return True

    # for idx in range(len(s)):
    #     in_dict = s[:idx+1] in wordDict and self.wordBreak(s[idx+1:], wordDict)
    #     if in_dict:
    #         return True

    # return False

    valid_words = [False] * (len(s)+1)
    valid_words[len(s)] = True

    for idx in reversed(range(len(s))):
        for word in wordDict:
            if idx + len(word) <= len(s) and s[idx:idx+len(word)] == word:
                valid_words[idx] = valid_words[idx+len(word)]

            if valid_words[idx]:
                break

    return valid_words[0]