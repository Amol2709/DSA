class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n= len(nums)
        p1=0
        p2=0
        count = 0
        ans = 0
        while(p2<=n-1):
            if nums[p2]==0:
                count = count +1
            if count>k:
                while(count>k):
                    if nums[p1]==0:
                        count = count-1
                    p1=p1+1
            
            ans =max(ans,p2-p1+1)
            p2=p2+1
            
            
        return ans
                
        