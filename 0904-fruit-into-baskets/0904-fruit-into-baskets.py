class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        answer = 0
        l = 0

        fruit_counts = defaultdict(int)
        for r in range(len(fruits)):
            curr_fruit = fruits[r]
            fruit_counts[curr_fruit] += 1

            while len(fruit_counts) > 2:
                fruit_to_remove = fruits[l]
                fruit_counts[fruit_to_remove] -= 1

                if fruit_counts[fruit_to_remove] == 0:
                    del fruit_counts[fruit_to_remove]

                l += 1        
            
            answer = max(answer, r - l + 1)
        
        return answer
