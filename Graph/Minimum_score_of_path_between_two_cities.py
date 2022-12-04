import sys
class Solution:
    def minScore(self, n: int, roads) -> int:
        # Leetcode: 2492
        adjList = {}
        for i in range(1,n+1):
            adjList[i]=[]
        for i in range(len(roads)):
            a,b,dist = roads[i][0],roads[i][1],roads[i][2]
            
            adjList[a].append((b,dist))
            adjList[b].append((a,dist))
        
        distance = [sys.maxsize]*(n+1)
        
        from collections import deque
        Q = deque()
        Q.append(1)
        
        while(Q):
            node = Q.popleft()
            
            _min = distance[node]
            for _ in adjList[node]:
                nextnode,dist = _
                _min  = min(_min,dist)
                
            for _ in adjList[node]:
                nextnode,dist = _
                if _min<distance[nextnode]:
                    distance[nextnode]=min(_min,distance[node])
                    Q.append(nextnode)
            
                    
                    
        if distance[n]!=sys.maxsize:
            return distance[n]
        return -1