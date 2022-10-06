import sys
class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        
        s = set(A)
        for i in range(1,max(A)+1):
            if i not in s:
                return i
        return max(max(A)+1,1)
        