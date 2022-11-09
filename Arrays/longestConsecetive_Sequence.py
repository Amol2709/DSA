class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        n = len(nums)
        if n ==0:
            return 0
        ans = 1
        for i in range(n):
            if nums[i]-1 not in s:
                elem = nums[i]
                tmp =0
                while(True):
                    if elem in s:
                        #print(elem,tmp)
                        elem = elem+1
                        ans = max(ans,tmp+1)
                        tmp+=1
                    else:
                        break
        return ans
                        
                    
                    
            
        