class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        low,high = max(nums),sum(nums)
        n = len(nums)
        if n==k:
            return max(nums)

        def check(target):
            curr_sum = nums[0]
            partion=0
            for i in range(1,n):
                curr_sum+=nums[i]

                if curr_sum>target:
                    partion+=1
                    curr_sum = nums[i]
            if partion+1<=k:
                return True
            return False
                    


        while(low<=high):
            mid = (low+high)//2

            if check(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans