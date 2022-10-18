'''
Given an array of integers A and an integer B, find and return the maximum value K
such that there is no subarray in A of size K
with the sum of elements greater than B.

'''
class Solution:
    def solve(self, A, B):
        self.prefix = [A[0]]
        self.B = B
        self.n = len(A)
        for i in range(1,self.n):
            self.prefix.append(self.prefix[-1]+A[i])
        low,high = 1,self.n
        self.ans = 0
        while(low<=high):
            mid = (low+high)//2
            if self.check(mid):
                self.ans = max(self.ans,mid)
                low = mid +1
            else:
                high = mid-1
        return self.ans
    
    def check(self,k):
        for i in range(k-1,self.n):
            if i-k>=0:
                if self.prefix[i]-self.prefix[i-k]>self.B:
                    return False
                    
            else:
                if self.prefix[i]>self.B:
                    return False
        return True


            
            
