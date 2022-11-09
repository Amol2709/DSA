class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        col_=len(A)
        for i in range(0,len(A)):
            for j in range(0,len(A[0])):
                if j>i:
                    temp=A[i][j]
                    A[i][j]=A[j][i]
                    A[j][i]=temp
        for i in range(0,len(A)):
            for j in range(0,int(col_/2)):
                temp=A[i][j]
                A[i][j]=A[i][col_-j-1]
                A[i][col_-j-1]=temp
        return A
