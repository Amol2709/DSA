class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k= k%n
        num= nums[n-k:]+nums[0:n-k]
        for i in range(len(num)):
            nums[i] = num[i]
        