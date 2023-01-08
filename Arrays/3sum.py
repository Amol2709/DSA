import sys
# new comment
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        curr_diff = sys.maxsize
        for i in range(n):
            ptr1,ptr2=i+1,n-1
            curr_target = target-nums[i]
            while(ptr1<ptr2):
                curr_sum = nums[i]+nums[ptr1]+nums[ptr2]
                if abs(target-curr_sum)<curr_diff:
                    ans = curr_sum
                    curr_diff = abs(target-curr_sum)
                
                
                

                if nums[ptr1]+nums[ptr2]>curr_target:
                    ptr2-=1
                else:
                    ptr1+=1
        return ans
