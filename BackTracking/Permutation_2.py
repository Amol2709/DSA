'''
Given a collection of numbers, nums, that might contain duplicates,
 return all possible unique permutations in any order.
'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.s = set()
        self.n = len(nums)
        self.map= set()
        self.ans = []
        self.myFunc(0,[])
        return self.ans
    def myFunc(self, count, tmp):
        if count == self.n:
            if tuple(tmp) not in self.s:
                self.ans.append(tmp)
                self.s.add(tuple(tmp))
            return
        for i in range(0,self.n):
            if i not in self.map:
                self.map.add(i)
                self.myFunc(count+1,tmp+[self.nums[i]])
                self.map.remove(i)
        
        