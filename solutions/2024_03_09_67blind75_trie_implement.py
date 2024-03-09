# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# all tests passed
class Trie:

    def __init__(self):
        self.children = {}
        self.end = False
        

    def insert(self, word: str) -> None:
        curr = self

        for idx in range(len(word)):
            c = word[idx]
            if c in curr.children:
                curr = curr.children[c]
                if idx == len(word)-1:
                    curr.end = True

            else:
                newnode = Trie()

                curr.children[c] = newnode
                curr = curr.children[c]
                if idx == len(word)-1:
                    curr.end = True
        

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                print(curr.children)
                print(curr.end)
            else:
                return False
        return curr.end


    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False

        return True