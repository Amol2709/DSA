class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        self.edge = []
        N = len(B)
        self.size=[1]*(A+1)
        self.parent = list(range(A+1))
        for i in range(N):
            x,y,wt = B[i][0],B[i][1],B[i][2]
            self.edge.append((wt,x,y))
        self.edge = sorted(self.edge)
        cost = 0
        for i in range(N):
            wt,node1,node2 = self.edge[i][0],self.edge[i][1],self.edge[i][2]
            if self.find(node1)!= self.find(node2):
                self.union(node1,node2)
                cost = cost+wt 
        return cost 
    
    def find(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    def union(self,node1,node2):
        par1 = self.find(node1)
        par2 = self.find(node2)
        if self.size[par1]==self.size[par2]:
            self.parent[par2]=par1
            self.size[par1]=self.size[par1]+1
            
        elif self.size[par1]>self.size[par2]:
            self.parent[par2]=par1
        else:
            self.parent[par1]=par2