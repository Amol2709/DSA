
'''

You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.
'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count_g=0
        ans=0
        for i in range(len(A)-1,-1,-1):
            if A[i]=='G':
                count_g+=1
            elif A[i]=='A':
                ans = ans+count_g
        return ans
