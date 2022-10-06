'''
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums=nums
        self.n = len(self.nums)
        self.s=set()
        self.ans=[]
        self.myFunc([])
        return self.ans
    def myFunc(self,tmp):
        if len(tmp)==self.n:
            self.ans.append(tmp)
            return
        for i in range(0,self.n):
            if i not in self.s:
                self.s.add(i)
                self.myFunc(tmp+[self.nums[i]])
                self.s.remove(i)
        