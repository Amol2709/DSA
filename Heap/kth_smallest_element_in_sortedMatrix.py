'''
Given a sorted matrix of integers A of size N x M and an integer B.

Each of the rows and columns of matrix A is sorted in ascending order, 
find the Bth smallest element in the matrix.

NOTE: Return The Bth smallest element in the sorted order, not the Bth distinct element.
'''

import heapq
class Solution:
    def solve(self, A, B):
        H =[]
        heapq.heapify(H)
        row,col = len(A),len(A[0])
        n = (row*col)-B+1

        for i in range(row):
            for j in range(col):
                if len(H)>=n:
                    if A[i][j]>=H[0]:
                        heapq.heappop(H)
                        heapq.heappush(H,A[i][j])
                else:
                    heapq.heappush(H,A[i][j])
        return H[0]
