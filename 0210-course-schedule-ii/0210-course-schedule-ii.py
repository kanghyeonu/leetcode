class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a) # [a, b] is b -> a
            indegree[a] += 1
        
        dq = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                dq.append(i)
        
        answer = []
        while dq:
            curr = dq.popleft()
            answer.append(curr)
            for i in graph[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    dq.append(i)
        
        return answer if len(answer) == numCourses else []