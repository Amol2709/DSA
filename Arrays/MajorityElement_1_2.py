######## Majority Element 1 ###############

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans_index = 0
        count = 1

        for i in range(1,len(nums)):
            if nums[i]==nums[ans_index]:
                count+=1
            else:
                count-=1
            

            if count == 0:
                ans_index = i 
                count = 1 
        return nums[ans_index]



########## Majority Element  2  ######################



class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        map_  = {}
        for i in A:
            if i in map_:
                map_[i] +=1
            else:
                map_[i]=1
        count_ = n//3
        for i in map_:
            if map_[i] >count_:
                return i 
        return -1



######### Optimize 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, nums):
        import sys

        elem1= -sys.maxsize
        elem2 = - sys.maxsize 

        count1 = 0
        count2 = 0

        for i in range(len(nums)):
            if nums[i]==elem1:
                count1+=1
            elif nums[i]==elem2:
                count2+=1
            elif count1 == 0:
                elem1 = nums[i]
                count1+=1
            elif count2 == 0:
                elem2 = nums[i]
                count2+=1
            else:
                count1-=1
                count2-=1
        count1=count2 = 0
        tmp = len(nums)//3
        for i in range(len(nums)):
            if nums[i]==elem1:
                count1+=1
            elif nums[i]==elem2:
                count2+=1
            if count1>tmp:
                return elem1
            if count2>tmp:
                return elem2 
        return -1
        

