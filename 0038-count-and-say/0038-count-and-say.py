class Solution:
    def countAndSay(self, n: int) -> str:
        def RLE(curr, target, answer):
            if curr == target:
                return answer
            
            cnt = 0
            num = answer[0]
            update = ""
            for c in answer:
                if c != str(num):
                    update += (str(cnt) + str(num))
                    num = int(c)
                    cnt = 1
                else:
                    cnt += 1
            update += (str(cnt) + str(num))

            return RLE(curr + 1, target, update)

        return RLE(1, n, "1")