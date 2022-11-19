class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        import math
        ans = 0
        for i in range(len(nums)):
            val = nums[i]
            if val == k:
                ans+=1
            for j in range(i+1,len(nums)):
                val = math.lcm(val,nums[j])
                if val == k:
                    ans+=1
        return ans
                
        