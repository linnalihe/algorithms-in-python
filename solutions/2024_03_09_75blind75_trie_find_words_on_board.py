# https://leetcode.com/problems/word-search-ii/
# all tests passed
class TrieTree():
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        curr = self
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieTree()
            curr = curr.children[c]
        curr.is_word = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        
        root = TrieTree()
        for word in words:
            root.add_word(word)

        rowlen = len(board)
        collen = len(board[0])
        visited = set()
        output = []

        def dfs_find_word(ridx, cidx, root, word):

            if (ridx < 0 or ridx >= len(board) or cidx < 0 
            or cidx >= len(board[0]) or (ridx, cidx) in visited 
            or (not board[ridx][cidx] in root.children)):
                return

            visited.add((ridx, cidx))
            node = root.children[board[ridx][cidx]]
            word = word+board[ridx][cidx]
            if node.is_word:
                output.append(word)
                node.is_word = False

            dfs_find_word(ridx+1, cidx, node, word)
            dfs_find_word(ridx-1, cidx, node, word)
            dfs_find_word(ridx, cidx+1, node, word)
            dfs_find_word(ridx, cidx-1, node, word)

            visited.remove((ridx, cidx))

        # go thru row and col to check if word in trie
        for rowidx in range(rowlen):
            for colidx in range(collen):
                dfs_find_word(rowidx, colidx, root, "")

        return output