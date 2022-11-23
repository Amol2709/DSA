'''
You are given an array A of N elements. 
You have to make all elements unique.
 To do so, in one step you can increase any number by one.

Find the minimum number of steps.

'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        N = len(A)
        count = 0
        for i in range(1,N):
            if A[i]<=A[i-1]:
                tmp = A[i]
                A[i] = A[i-1]+1
                count += A[i]-tmp 
        return count