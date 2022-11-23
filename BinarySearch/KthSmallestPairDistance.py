'''

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, 
return the kth smallest distance among all the pairs nums[i] and nums[j]
where 0 <= i < j < nums.length.

''' 



class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def check(tmp):
            ans = 0
            ptr1,ptr2  = 0,1
            n = len(nums)
            while(ptr1<n):
                while(ptr2<n and nums[ptr2]-nums[ptr1]<=tmp):
                    ptr2 = ptr2+1
                ans = ans +ptr2-ptr1-1
                ptr1 = ptr1+1
            return ans
        
        nums = sorted(nums)
        low, high = 0, nums[-1]-nums[0]
        
        while(low<=high):
            mid = (low+high)//2
            tmp = check(mid)
            if tmp<k:
                low = mid+1
            else:
                ans = mid
                high = mid-1
                
        return ans
                