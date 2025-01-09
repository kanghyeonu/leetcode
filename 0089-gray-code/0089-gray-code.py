class Solution:
    def grayCode(self, n: int) -> List[int]:
        answer = []
        num = 0

        while num <= 2**n-1:
            answer.append(num ^ (num >> 1))
            print(num ^ (num >> 1))
            num += 1
        return answer
       

            
        
