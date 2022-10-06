'''
Leetcode: 1823
'''

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums = list(range(1,n+1))
        k = k-1
        pos = 0
        
        while(True):
            if n==1:
                return nums[0]
            pos = pos + k #jump
            if pos>=n:
                pos = pos%n 
            
            if pos+1<n:
                nums = nums[0:pos]+nums[pos+1:]
            else:
                nums = nums[0:pos]
            n = n-1
                