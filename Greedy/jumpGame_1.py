class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        target_index = n-1
        curr_index = n-2
        while(curr_index>=0):
            if target_index-curr_index<= nums[curr_index]:
                target_index,curr_index = curr_index,curr_index-1
            else:
                curr_index = curr_index-1
        if target_index<=0:
            return True
        return False
        