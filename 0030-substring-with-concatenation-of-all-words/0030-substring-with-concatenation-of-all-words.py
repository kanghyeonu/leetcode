import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answer = []
        words_cnt = collections.Counter(words)
        n = len(words[0])
        words_length = len(words) * n
        
        for i in range(len(s) - words_length + 1):
            seen = collections.defaultdict(int)
            w = i
            while w < w + words_length:
                word = s[w:w+n]
                seen[word] += 1
                if seen[word] > words_cnt[word]:
                    break            
                w += n

            if i + words_length == w:
                answer.append(i)        
  
        return answer
