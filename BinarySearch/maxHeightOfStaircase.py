class Solution:
    def solve(self, A):
        if A==0:
            return 0
        low,high = 1,A**2
        while(low<=high):
            mid = (low+high)//2

            if (mid*(mid+1))/2<=A:
                low = mid+1
                ans  = mid
            else:
                high = mid-1
        return ans

