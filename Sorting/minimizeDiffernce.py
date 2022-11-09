import sys
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dp = [0]*(max(A)+1)
        mi= sys.maxsize
        ma = -sys.maxsize

        for i in range(0,len(A)):
            dp[A[i]]+=1
            if A[i]<mi:
                mi = A[i]
            if A[i]>ma:
                ma = A[i]
        i,j = mi,ma
        ans = j-i
        freqMin,freqMax = dp[mi],dp[ma]

        while(i<j):
            if B<min(freqMax,freqMin):
                break
            if freqMin<freqMax:
                B = B-freqMin
                freqMin+=dp[i+1]
                i+=1
            else:
                B = B-freqMax
                freqMax+=dp[j-1]
                j=j-1
            ans = j-i
        return ans
