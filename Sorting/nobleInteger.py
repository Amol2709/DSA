
'''

Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.
'''

class Solution:
    def solve(self, A):
        A=sorted(A)
        if A[-1]==0:
            return 1
        for i in range(0,len(A)-1):
            if A[i]<0:
                continue
            if A[i]!=A[i+1] and A[i]==((len(A)-i)-1):
                return 1
        return -1
