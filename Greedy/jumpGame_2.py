class Solution(object):
    def jump(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right = 0,0
        n = len(arr)
        if n==0:
            return 0
        ans  =0
        while(right<n-1):
            farthest = 0
            for i in range(left,right+1):
                farthest = max(farthest,arr[i]+i)
            left = right+1
            right = farthest
            ans = ans+1
        return ans