class Solution:
    def countPrimes(self, n: int) -> int:
        
        isPrime = [True for x in range(n)]
        p = 2
        while p * p < n:
            if isPrime[p]:
                for i in range(p * p, n, p):
                    isPrime[i] = False
            p += 1

        answer = 0
        for i in range(2, n):
            if isPrime[i]:
                answer += 1
                
        return answer
