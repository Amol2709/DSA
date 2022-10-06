from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def motherVertex(self, A, B):
        self.adjList = {}
        for i in range(1,A+1):
            self.adjList[i]=set()
        
        for i in range(len(B)):
            if B[i][0]!=B[i][1]:
                self.adjList[B[i][0]].add(B[i][1])
        self.visarr = set()
        self.stk = []
        self.count = 0
        for node in range(1,A+1):
            if node not in self.visarr:
                self.visarr.add(node)
                self.applydfs(node)
        node = self.stk[-1]
        self.count = 0
        self.visarr = set()
        self.applydfs2(node)
        if self.count == A:
            return 1
        return 0
    def applydfs2(self,node):
        self.visarr.add(node)
        self.count+=1
        for _ in self.adjList[node]:
            if _ not in self.visarr:
                self.visarr.add(_)
                self.applydfs2(_)
            
        
    def applydfs(self,node):
        self.visarr.add(node)
        self.count+=1
        for _ in self.adjList[node]:
            if _ not in self.visarr:
                self.visarr.add(_)
                self.applydfs(_)
        self.stk.append(node)