class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        check = [False for _ in range(len(nums))]

        def dfs(p):
            if len(p) == len(nums) and p not in answer:
                answer.append(p)
            
            for i in range(len(nums)):
                if check[i]:
                    continue
                check[i] = True
                dfs(p + [nums[i]])
                check[i] = False
            
        dfs([])
        
        return answer
        
