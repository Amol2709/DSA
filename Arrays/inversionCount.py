class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, nums):
        self.nums=nums
        N= len(nums)
        self.count=0
        if N==1:
            return 0
        self.ans = [-1]*N
        
        return int(self.func(0,N-1) % (1e9+7))
    def func(self,L,R):
        if L==R:
            return 0
        mid_ = int((L+R)/2)
        count=0
        count = count+self.func(L,mid_)
        count = count+self.func(mid_+1,R)
        count = count+self.Merge(L,mid_,R)
        #print(self.ans)
        return count
    def Merge(self,start,mid,end):
        p1 = start
        p2 = mid+1
        i=p1
        inv_count=0
        while(p1<=mid and p2<=end):
            if self.nums[p1]<=self.nums[p2]:
                self.ans[i]=self.nums[p1]
                p1=p1+1
                i=i+1
            else:
                self.ans[i]=self.nums[p2]
                i=i+1
                p2=p2+1
                inv_count = inv_count + (mid-p1+1)
        while(p2<=end):
            self.ans[i]=self.nums[p2]
            i=i+1
            p2 = p2+1
        while(p1<=mid):
            self.ans[i]=self.nums[p1]
            p1=p1+1
            i=i+1
        for i in range(start,end+1):
            self.nums[i]=self.ans[i]
        return inv_count
