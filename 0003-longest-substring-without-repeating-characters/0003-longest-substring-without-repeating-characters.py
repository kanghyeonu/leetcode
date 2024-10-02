class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = ""
        l = 0
        for char in s:
            index = subs.find(char)
            if index >= 0:
                subs = subs[index+1:]
                subs += char
            else:
                subs += char
                if len(subs) > l:
                    l += 1
                    
        return l