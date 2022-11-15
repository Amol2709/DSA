class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high = 0, len(nums)-1
        ans = nums[0]
        while(low<=high):
            mid = (low+high)//2
            
            if nums[0]>nums[mid]:
                ans = nums[mid]
                high = mid-1
            else:
            
                low = mid+1
        return ans