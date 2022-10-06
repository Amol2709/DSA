class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        self.A = sorted(A) 
        self.B = B
        self.n = len(A)
        self.s = set()
        self.ans = []
        self.func(0,self.B,[])
        return self.ans
    def func(self,index,target,tmp):
        if target == 0:
            tmp2 = tuple(tmp)
            if tmp2 not in self.s:
                self.ans.append(tmp)
                self.s.add(tmp2)
            return
        if index>=self.n:
            return 
        self.func(index+1,target,tmp)
        if target-self.A[index]>=0:
            self.func(index+1,target-self.A[index],tmp+[self.A[index]])

