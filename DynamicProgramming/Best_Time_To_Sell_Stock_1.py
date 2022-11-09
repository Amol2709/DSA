class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        import sys
        buy = sys.maxsize
        profit  = -sys.maxsize
        N = len(A)
        if N==0 or N==1:
            return 0
        for i in range(0,N):
            buy = min(buy,A[i])
            profit =max(profit,(A[i]-buy))
        return profit

