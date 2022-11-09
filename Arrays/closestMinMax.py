'''
Given an array A, find the size of the smallest subarray such that it contains at 
least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        import sys
        A_length = len(A)
        
        if A_length == 1:
            return 1
        
        min_val,max_val = min(A),max(A)
        
        ans = sys.maxsize
        min_index = -1
        max_index = -1
        
        for index in range(A_length):
            
            if A[index] == min_val:
                min_index = index
            
            if A[index] == max_val:
                max_index = index
            if min_index!=-1 and max_index!=-1:
                ans = min(ans, abs(max_index-min_index)+1)
        
        return max(1,ans)
        
