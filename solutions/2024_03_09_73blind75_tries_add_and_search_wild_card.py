# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# all tests passed
class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
        
        curr.is_word = True
        

    def search(self, word: str) -> bool:

        def dfs(idx, node):
            curr = node
            for nxtidx in range(idx, len(word)):
                if word[nxtidx] == ".":
                    for child in curr.children:
                        if dfs(nxtidx+1, curr.children[child]):
                            return True
                    return False
                
                else:
                    if word[nxtidx] in curr.children:
                        curr = curr.children[word[nxtidx]]
                    else:
                        return False
        
            return curr.is_word
        
        return dfs(0, self.root)