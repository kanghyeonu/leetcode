class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # 시작 단어 -> 접근 가능한 시퀀스 단어 찾기
        reachable = []
        for word in wordList:
            if self.isReachable(beginWord, word):
                reachable.append(word)
        
        # 접근 가능한게 없으면 답없음
        if not reachable:
            return 0
        elif endWord in reachable:
            return 2

        notVisited = set(wordList)
        notVisited.discard(endWord)
        notVisited.discard(beginWord)

        dq = deque([endWord])
        found = False
        step = 1
       
        while(dq and not found):
            step += 1
            for _ in range(len(dq)):
                word = dq.popleft()

                visited = set()
                for w in notVisited:
                    if not self.isReachable(word, w):
                        continue
                    dq.append(w)
                    visited.add(w)

                    if w in reachable:
                        found = True
                        return step + 1

                notVisited = notVisited - visited

        return 0



    def isReachable(self, w1, w2):
        count = 0
        for w1_char, w2_char in zip(w1, w2):
            if w1_char != w2_char:
                count += 1
        
        return True if count ==1 else False