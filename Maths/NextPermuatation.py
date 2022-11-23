class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        12345
        12354
        12435
        12453
        12534
        12543

        13245
        13254
        13425
        13452



        54321

        """
        n = len(nums)
        index = -1
        for i in range(n-1,0,-1):
            if nums[i]>nums[i-1]:
                index = i-1
                break
        if index ==-1:
            ptr1,ptr2 = 0,n-1
            while(ptr1<ptr2):
                nums[ptr1],nums[ptr2] = nums[ptr2],nums[ptr1]
                ptr1+=1
                ptr2-=1
        else:
            
            for i in range(n-1,-1,-1):
                if nums[i]>nums[index]:
                    index2 = i 
                    break
            nums[index],nums[index2] = nums[index2],nums[index]

            ptr1,ptr2 = index+1,n-1
            while(ptr1<ptr2):
                nums[ptr1],nums[ptr2] = nums[ptr2],nums[ptr1]
                ptr1+=1
                ptr2-=1
            