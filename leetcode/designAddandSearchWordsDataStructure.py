# Medium

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


# Constraints:

# 1 <= word.length <= 500
# word in addWord consists lower-case English letters.
# word in search consist of  '.' or lower-case English letters.
# At most 50000 calls will be made to addWord and search.

# Runtime: 388 ms, faster than 20.16% of Python3 online submissions for Design Add and Search Words Data Structure.
# Memory Usage: 31 MB, less than 7.47% of Python3 online submissions for Design Add and Search Words Data Structure.

class Node:
    def __init__(self, char):
        self.value = char
        self.endOfWord = False
        self.nodeArray = [None]*26


class WordDictionary:

    def __init__(self):
        self.root = Node("")
        """
        Initialize your data structure here.
        """

    def addWord(self, word: str) -> None:
        # for each letter in the word, check if there is a node for it
        # if there is a node, go to the next node
        # otherwise create new node and add it to the list, and if it is the last letter,
        curr = self.root
        for i in range(len(word)):
            nodeIndex = ord(word[i].lower())-ord('a')
            if(curr.nodeArray[nodeIndex]):
                curr = curr.nodeArray[nodeIndex]
            else:
                newNode = Node(word[i])
                curr.nodeArray[nodeIndex] = newNode
                curr = newNode
                if(i == len(word)-1):
                    curr.endOfWord = True

    def search(self, word: str) -> bool:
        nodes = [self.root]

        for char in word:

            nodeIndex = ord(char.lower()) - ord('a')
            nextNodes = []
            for node in nodes:

                if char == '.':
                    for each in node.nodeArray:
                        if each:
                            nextNodes.append(each)
                    continue
                if node.nodeArray[nodeIndex]:
                    nextNodes.append(node.nodeArray[nodeIndex])

            nodes = nextNodes

        for node in nodes:
            if node.endOfWord:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Resources to check out
# https://www.tutorialspoint.com/implement-trie-prefix-tree-in-python
# https://albertauyeung.github.io/2020/06/15/python-trie.html
