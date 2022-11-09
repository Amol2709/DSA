class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        ans=0
        row_=len(A)
        col_=len(A[0])
        for i in range(0,len(A)):
            for j in range(0,len(A[0])):
                ans= ans+A[i][j]*(i+1)*(row_-i)*(j+1)*(col_-j)
        return ans

