class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        import sys
        ans = -sys.maxsize
        curr_sum = 0
        for i in range(0,len(A)):
            curr_sum = curr_sum +A[i]
            ans = max(ans,curr_sum)
            if curr_sum <0:
                curr_sum =0
        return ans
