from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        self.A = A 
        self.row,self.col = len(self.A),len(self.A[0])
        ans = 0
        self.blueLakedp=[[False for i in range(self.col)] for j in range(self.row)]
        self.redLakedp = [[False for i in range(self.col)] for j in range(self.row)]
        rowPos = [0,1,0,-1]
        colPos = [1,0,-1,0]
        bluelakeQ  = deque()
        redlakeQ = deque()
        for i in range(0,self.col):
            self.blueLakedp[0][i]=True
            self.redLakedp[self.row-1][i]=True
            bluelakeQ.append((0,i))
            redlakeQ.append((self.row-1,i))
            
        for i in range(0,self.row):
            self.blueLakedp[i][0]=True
            self.redLakedp[i][self.col-1]=True
            bluelakeQ.append((i,0))
            redlakeQ.append((i,self.col-1))
        
        while(len(bluelakeQ)!=0):
            r,c = bluelakeQ.popleft()
            for i in range(0,4):
                x,y = r+rowPos[i], c+colPos[i]
                if 0<=x<self.row and 0<=y<self.col and self.A[r][c]<=self.A[x][y] and self.blueLakedp[x][y]==False:
                    self.blueLakedp[x][y] = True
                    bluelakeQ.append((x,y))
        
        while(len(redlakeQ)!=0):
            r,c = redlakeQ.popleft()
            for i in range(0,4):
                x,y = r+rowPos[i], c+colPos[i]
                if 0<=x<self.row and 0<=y<self.col and self.A[r][c]<=self.A[x][y] and self.redLakedp[x][y]==False:
                    self.redLakedp[x][y] = True
                    redlakeQ.append((x,y))
        
        for i in range(0,self.row):
            for j in range(0,self.col):
                if self.redLakedp[i][j] and self.blueLakedp[i][j]:
                    ans = ans +1
        return ans
    

