class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        n = len(nums)
        prefix_set={}
        
        curr_sum = 0
        for i in range(n):
            curr_sum= curr_sum+ nums[i]
            
            if curr_sum ==k :
                ans  = ans+1
            if curr_sum-k in prefix_set:
                ans = ans+prefix_set[curr_sum-k]
            
            ####Update######
            if curr_sum in prefix_set:
                prefix_set[curr_sum]=prefix_set[curr_sum]+1
            else:
                prefix_set[curr_sum]=1
        return ans
            
            
            
        