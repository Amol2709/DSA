from collections import deque

class Solution:
    def black(self, A):
        Q = deque()
        row,col = len(A),len(A[0])
        visArr = [[False for i in range(col)]for j in range(row)]
        adjRow = [0,1,0,-1]
        adjCol = [1,0,-1,0]
        ans = 0


        for i in range(row):
            for j in range(col):
                if A[i][j]=='X' and visArr[i][j]==False:
                    Q.append((i,j))
                    ans = ans+1
                    while(len(Q)!=0):
                        r,c = Q.popleft()
                        for pos in range(0,4):
                            next_r = r+adjRow[pos]
                            next_c = c+adjCol[pos]

                            if 0<=next_r<row and 0<=next_c<col and A[next_r][next_c]=='X' and visArr[next_r][next_c]==False:
                                visArr[next_r][next_c]=True
                                Q.append((next_r,next_c))
        return ans



