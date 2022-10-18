class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        # T.c = O[n]
        # for i in range(len(A)):
        #     for j in range(len(A[0])):
        #         if A[i][j]==B:
        #             return 1
        # return 0

        # T.c = o[m+n]
        # row =-1
        # for i in range(len(A)):
        #     if A[i][-1]>=B:
        #         row  = i
        #         break
        # if row ==-1:
        #     return 0
        # for j in range(len(A[0])):
        #     if A[row][j]==B:
        #         return 1
        # return 0
        row,col = len(A),len(A[0])
        low,high =0,(row*col)-1

        while(low<=high):
            mid = (low+high)//2
            r,c = mid//col,int(mid%col)
            if A[r][c]==B:
                return 1
            if A[r][c]<B:
                low = mid+1
            else:
                high = mid-1
        return 0




