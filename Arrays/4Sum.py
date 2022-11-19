class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        s = set()
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                curr_target = target-(nums[i]+nums[j])
                ptr1,ptr2 = j+1,n-1
                while(ptr1<ptr2):
                    if nums[ptr1]+nums[ptr2]== curr_target and (nums[i],nums[j],nums[ptr1],nums[ptr2]) not in s:
                        ans.append([nums[i],nums[j],nums[ptr1],nums[ptr2]])
                        s.add((nums[i],nums[j],nums[ptr1],nums[ptr2]))
                    elif nums[ptr1]+nums[ptr2]> curr_target:
                        ptr2-=1
                    else:
                        ptr1+=1
        return ans