class Solution:
    def maxProduct(self, nums: 'List[int]') -> 'int':
        # init
        results = [(nums[0], nums[0])]
        
        for i in range(1, len(nums)):
            # 연속 곱 계산 -> 연속 곱의 최대, 최소 연산
            temp1 = nums[i] * results[i-1][0] # 최대 값
            temp2 = nums[i] * results[i-1][1] # 최소 값

            # 새 값, 연속 곱 값 비교 후 갱신
            big = max(nums[i], temp1, temp2)
            small = min(nums[i], temp1, temp2)

            results.append((big, small))

        return max(x for x, _ in results)