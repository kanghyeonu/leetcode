class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        index = [0] * len(primes)
        val = [1] * len(primes)
        
        for i in range(1, n):
            last = ugly[i-1]
            candidate = float('inf')
            for j, p in enumerate(primes):
                if val[j] == last:
                    val[j] = p * ugly[index[j]]
                    index[j] += 1
                candidate = min(candidate, val[j])
            
            ugly[i] = candidate

        return ugly[n-1]



