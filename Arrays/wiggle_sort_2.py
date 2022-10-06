'''
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
'''


def wiggleSort(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    n = len(nums)
    arr = [-1]*n
    nums.sort()
    index = n-1
    for i in range(1,n,2):
        arr[i] = nums[index]
        index = index-1
    for i in range(0,n,2):
        arr[i] = nums[index]
        index = index-1
    for i in range(n):
        nums[i]=arr[i]
    