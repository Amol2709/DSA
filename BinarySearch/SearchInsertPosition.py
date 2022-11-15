class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        leetcode:35
        """
        if target>nums[-1]:
            return len(nums)
        if target<nums[0]:
            return 0
        low,high = 0,len(nums)-1

        while(low<=high):
            mid = (low+high)//2
            if nums[mid]==target:
                return mid 
            elif nums[mid]>target:
                high = mid-1
                ans = mid
            else:
                low = mid+1
        return ans
