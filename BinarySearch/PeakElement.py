'''
leetcode: 162
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high = 0, len(nums)-1
        n = len(nums)
        if n==1:
            return 0
        while(low<=high):
            mid = (low+high)//2
            
            if mid-1>=0 and mid+1<=n-1 and  nums[mid]>nums[mid-1] and nums[mid]>=nums[mid+1]:
                return mid
            if mid+1<=n-1 and nums[mid]<nums[mid+1]:
                low = mid+1
            else:
                high = mid-1
        if nums[0]>nums[1]:
            return 0
        else:
            return n-1
        
        
        