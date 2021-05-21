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

import string


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
        currentNode = self.root
        for i in range(len(word)):
            nodeIndex = ord(word[i].lower())-ord('a')
            if(currentNode.nodeArray[nodeIndex]):
                currentNode = currentNode.nodeArray[nodeIndex]
            else:
                newNode = Node(word[i])
                currentNode.nodeArray[nodeIndex] = newNode
                currentNode = newNode
                if(i == len(word)-1):
                    currentNode.endOfWord = True

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

# solution below based on discussion post by https://leetcode.com/b10232021/

class WordDictionary:
    def __init__(self):
        # initializes class WordDictionary2 with a table that is a dictionary
        # each key of the dictionary is a character in the alphabet, each value of the key is a empty dictionary
        self.table = {char: dict() for char in string.ascii_lowercase}

    def addWord(self, word: str) -> None:
        lenOfWord = len(word)  # length of the input word
        firstCharOfWord = word[0]  # first character in the input word
        # self.table[firstCharOfWord] is getting the dictionary for the first character of input word
        if lenOfWord not in self.table[firstCharOfWord]:
            # create a key equal to lenOfWord in the dictionary associated with the letter of first char in input
            # set this key equal to the word
            self.table[firstCharOfWord][lenOfWord] = [word]
        else:
            # if there is already a key for the lenOfWord, add the word to the array associated with the key
            self.table[firstCharOfWord][lenOfWord].append(word)

    def search(self, word: str) -> bool:
        lenOfWord = len(word)
        pattern = list()
        # go through the word and add index and character to list
        # exclude the "." values
        # this is so that we can use this for checking if the words match in the 2nd for loop within this function
        for idx, char in enumerate(word):
            char != "." and pattern.append([idx, char])

        # go through all letters of the alphabet and get all words with the same length as input word
        # for each of the words that has been added, iterate through and compare with the pattern list
        # return true if there is a match out of all the words in the able otherwise return false
        for letter in string.ascii_lowercase:
            if lenOfWord in self.table[letter]:
                for entry in self.table[letter][lenOfWord]:
                    match = True
                    for idx, char in pattern:
                        if entry[idx] != char:
                            match = False

                    if match:
                        return True
        return False
