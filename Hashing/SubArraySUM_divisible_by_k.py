class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        leetcode:974
        :type nums: List[int]
        :type k: int
        :rtype: int
        [4,5,0,-2,-3,1]
        [4,9,9,7,4,5]
        [4,4,4,2,4,0]
        
        """
        _map = {}
        curr_sum = 0 
        ans = 0

        for i in range(len(nums)):
            curr_sum+=nums[i]

            mod = curr_sum%k
            if mod in _map:
                ans = ans+ _map[mod]
                _map[mod]+=1
            else:
                _map[mod]=1
            
            if curr_sum%k==0:
                ans+=1
        return ans
        