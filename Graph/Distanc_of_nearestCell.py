'''
Given a matrix of integers A of size N x M consisting of 0 or 1.

For each cell of the matrix find the distance of nearest 1 in the matrix.

Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.

Find and return a matrix B of size N x M which defines 
for each cell in A distance of nearest 1 in the matrix A.

NOTE: There is atleast one 1 is present in the matrix


'''


from collections import deque
import sys
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        Q = deque()
        row,col = len(A),len(A[0])
        #visArr = [[False for i in range(col)]for j in range(row)]
        B = [[sys.maxsize for i in range(col)]for j in range(row)]
        adjRow = [0,1,0,-1]
        adjCol = [1,0,-1,0]
     


        for i in range(row):
            for j in range(col):
                if A[i][j]== 1:
                    B[i][j]= 0
                    Q.append((i,j))
        while(len(Q)!=0):
            r,c = Q.popleft()
            for pos in range(0,4):
                next_r = r+adjRow[pos]
                next_c = c+adjCol[pos]
                if 0<=next_r<row and 0<=next_c<col and A[next_r][next_c]!=1:
                    dist = abs(r-next_r)+abs(c-next_c)
                    if dist+B[r][c]<B[next_r][next_c] :
                        B[next_r][next_c] = dist+B[r][c]
                        Q.append((next_r,next_c))
        return B




