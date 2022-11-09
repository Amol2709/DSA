class Solution:
    def minPathSum(self, A):
        self.A = A 
        self.row,self.col = len(A),len(A[0])
        self.dp=[[-1 for i in range(self.col)] for i in range(self.row)]
        #return self.func(self.row-1,self.col-1)
        self.dp[0][0] = self.A[0][0]
        for i in range(1,self.col):
            self.dp[0][i] = self.A[0][i]+self.dp[0][i-1]
        for i in range(1,self.row):
            self.dp[i][0] = self.A[i][0]+self.dp[i-1][0]

        for r in range(1,self.row):
            for c in range(1,self.col):
                self.dp[r][c] =  min(self.A[r][c]+self.dp[r][c-1],self.A[r][c]+self.dp[r-1][c])
        return self.dp[self.row-1][self.col-1]

    # def func(self,r,c):
    #     if r==c==0:
    #         return self.A[0][0]
    #     if (r<0 or r>=self.row) or (c<0 or c>=self.col):
    #         return sys.maxsize
    #     if self.dp[r][c]!=-1:
    #         return self.dp[r][c]
    #     self.dp[r][c] =  min(self.A[r][c]+self.func(r,c-1),self.A[r][c]+self.func(r-1,c))
    #     return self.dp[r][c]
