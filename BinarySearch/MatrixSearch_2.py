
''''
Given a matrix of integers A of size N x M and an integer B.
In the given matrix every row and column is sorted in non-decreasing order.
 Find and return the position of B in the matrix in the given form:
If A[i][j] = B then return (i * 1009 + j)
If B is not present return -1.

Note 1: Rows are numbered from top to bottom and columns are numbered from left to right.
Note 2: If there are multiple B in A then return the smallest value of i*1009 +j such that A[i][j]=B.
Note 3: Expected time complexity is linear
Note 4: Use 1-based indexing

'''


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def applyBinarySearch(self,r):
        low,high = 0,self.col-1
        self.flag = False

        while(low<=high):
            mid = (low + high)//2
            if self.A[r][mid]==self.B:
                self.flag  = True
                self.j = mid
                high = mid-1
            elif self.A[r][mid]>self.B:
                high = mid-1
            else:
                low = mid+1
        return self.flag

    def solve(self, A, B):
        self.A ,self.B= A, B
        self.row,self.col = len(A),len(A[0])
        for i in range(0,self.row):
            if self.applyBinarySearch(i):
                return (((i+1)*1009) + self.j+1)
        return -1



