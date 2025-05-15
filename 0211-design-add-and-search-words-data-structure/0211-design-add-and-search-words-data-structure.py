class WordDictionary:

    def __init__(self):
        self.root = dict()
        self.root["isEnd"] = False

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = dict()
                curr[char]["isEnd"] = False
            curr = curr[char]
        curr["isEnd"] = True
            

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        found = False
        while not found and stack:
            curr, index = stack.pop()
            if index == len(word):
                found = curr["isEnd"]
                continue
            
            char = word[index]
            if char == ".":
                for child in curr:
                    if child == "isEnd":
                        continue
                    stack.append((curr[child], index + 1))
            elif char in curr:
                next = curr[char]
                stack.append((next, index+1))
        return found



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)