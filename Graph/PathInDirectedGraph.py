from collections import deque

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adjList = {}
        for i in range(1,A+1):
            adjList[i]=[]
            
        for i in range(len(B)):
            adjList[B[i][0]].append(B[i][1])
        
        visNode = [False]*(A+1)   
        Q = deque()
        Q.append(1)
        
        while(len(Q)!=0):
            node = Q.popleft()
            if node == A:
                return 1
                
            visNode[node] = True
            for tmpNode in adjList[node]:
                if visNode[tmpNode]==False:
                    Q.append(tmpNode)
                    
                
        return 0
        
