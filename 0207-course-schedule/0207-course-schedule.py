class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #prerequisite[a, b] a를 듣기위해 b가 선행 b -> a
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        dq = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                dq.append(i)

        cnt = 0
        while dq:
            curr = dq.popleft()
            cnt += 1
            for i in graph[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    dq.append(i)
        
        return True if cnt == numCourses else False
