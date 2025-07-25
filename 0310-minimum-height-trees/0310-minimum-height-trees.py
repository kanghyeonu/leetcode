class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 리프 노드 체크
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        # MHT의 중심 노드 항상 1 or 2
        # 그래프의 리프부터 하나씩 제거하면서 중심 노드 후보 추리기
        while n > 2:
            n -= len(leaves) # 현 리프 노드 제거후 남은 노드 수
            new_leaves = [] # 새 리프 후보
            for leaf in leaves:
                neighbor = graph[leaf].pop() # 리프와 연결된 노드
                graph[neighbor].remove(leaf) # 연결된 노드에서 해당 리프 제거

                # 제거 후, 연결된 노드가 리프가 된다면 새 리프에 추가
                if len(graph[neighbor]) == 1: 
                    new_leaves.append(neighbor)

            leaves = new_leaves
        
        return leaves
        
