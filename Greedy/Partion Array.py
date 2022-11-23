class Solution(object):
    # LC: 561
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i  in range(len(nums)-2,-1,-2):
            ans +=min(nums[i],nums[i+1])
        return ans
