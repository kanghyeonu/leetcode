class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        rows, cols = len(board), len(board[0])
        result = []
        visited = set()

        def dfs(row, col, node):
            if node.word:
                result.append(node.word)
                node.word = None 

            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or board[row][col] not in node.children:
                return

            visited.add((row, col))
            dfs(row + 1, col, node.children[board[row][col]])
            dfs(row - 1, col, node.children[board[row][col]])
            dfs(row, col + 1, node.children[board[row][col]])
            dfs(row, col - 1, node.children[board[row][col]])
            visited.remove((row, col))

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, trie.root)

        return result