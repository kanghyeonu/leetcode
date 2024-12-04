class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort(key=lambda x: x[0])

        for lst in intervals:
            if len(answer) == 0:
                answer.append(lst)
                continue
        
            if answer[-1][1] >= lst[0]:
                if answer[-1][1] >= lst[1]:
                    pass
                else:
                    answer[-1][1] = lst[1]
            else:
                answer.append(lst)
        
        return answer
            

        