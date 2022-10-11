'''

Given two integers A and B, return all possible combinations of B numbers out of 1 2 3 ... A.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
'''


class Solution:
    def combine(self, A, B):
        self.B, self.A = B,A
        self.nums = list(range(1,A+1))
        self.ans = []
        self.s = set()
        self.myFunc(0,[],0)
        return self.ans

    def myFunc(self,index,tmp,count):
        if count == self.B:
            self.ans.append(tmp)
            return
        for i in range(index,self.A):
            if i not in self.s:
                self.s.add(i)
                self.myFunc(i+1,tmp+[self.nums[i]],count+1)
                self.s.remove(i)
                


