class Solution:
    def cmp(self, x, y):
        if x + y < y + x: # 
            return 1 # x가 더 작음 -> 뒤로
        else:
            return -1 # x가 더 큼 -> 앞으로 

    def largestNumber(self, nums: List[int]) -> str:
        nums_str = sorted(list(map(str, nums)), key=cmp_to_key(self.cmp))

        if nums_str[0] == "0":
            return "0"

        return "".join(nums_str)
        