'''
Leetcode: 376
'''


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pos_wig = [1]*n
        neg_wig = [1]*n
        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    pos_wig[i] = max(pos_wig[i],1+neg_wig[j])
                elif nums[j]<nums[i]:
                    neg_wig[i]=max(neg_wig[i],1+pos_wig[j])
        return max(max(pos_wig),max(neg_wig))
        