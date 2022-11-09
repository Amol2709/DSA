'''
Leetcode: 376
[1,17,5,10,13,15,10,5,16,8]
[1,1,1,1,1,1,1,3,1,1] =pos
[1,1,1,1,1,1,1,1,2,1] = neg

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
        


