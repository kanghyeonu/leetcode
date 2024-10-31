class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answer = []
        
        words_cnt = {}
        for word in words:
            if word in words_cnt:
                words_cnt[word] += 1
            else:
                words_cnt[word] = 1

        n = len(words[0])
        words_length = len(words) * n
        for i in range(len(s) - words_length + 1):
            copied = words_cnt.copy()
            w = i
            dup = ""
            while w < w + words_length:
                word = s[w:w+n]
                if not word in words_cnt:
                    break

                if copied[word] == 0:
                    dup = word
                    break
            
                copied[word] -= 1
                w += n

            if sum(copied.values()) == 0:
                answer.append(i)        
  
        return answer