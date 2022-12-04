class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        ptr1,ptr2 = 1,1
        nums = [0]+nums
        n = len(nums)
        ans = 0
        
        prefix_sum = [nums[0]]
        for i in range(1,n):
            prefix_sum.append(prefix_sum[-1]+nums[i])
        
        
        _map = {}
        
        while(ptr2<n):
    
            if nums[ptr2] not in _map:
                _map[nums[ptr2]]=ptr2
                
                if ptr2-ptr1+1>k:
                    del _map[nums[ptr1]]
                    ptr1+=1
                    
            else:
                prev_ptr1 = ptr1
                for i in range(ptr1,_map[nums[ptr2]]):
                    if nums[i] in _map :
                        del _map[nums[i]]
                        
                ptr1 = max(_map[nums[ptr2]]+1,ptr1+1)
                _map[nums[ptr2]]=ptr2
            
            

                
            #print(ptr2,ptr1)
            if ptr2-ptr1+1==k:
                ans = max(ans,prefix_sum[ptr2]-prefix_sum[ptr1-1])
            ptr2+=1
        return ans

        