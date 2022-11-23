class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        curr_max,curr_min=1,1
        for n in nums:
            tmp = curr_max
            curr_max = max(n*curr_max,n*curr_min,n)
            curr_min = min(n*tmp,n*curr_min,n)
            res = max(res,curr_max)
        return res
        