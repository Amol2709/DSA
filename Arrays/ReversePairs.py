class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        self.A = A
        self.count=0
        self.divide(0,len(A)-1)
        #print(self.A)
        return self.count
    def divide(self,low,high):
        if low>=high:
            return 
        mid = (low+high)//2
        self.divide(low,mid)
        self.divide(mid+1,high)
        self.MergeSort(low,mid,high)
    def check(self,arr1,arr2):
        ptr1,ptr2 = len(arr1)-1,len(arr2)-1
        
        while(ptr1>=0 and ptr2>=0):
            if arr1[ptr1]>2*arr2[ptr2]:
                tmp_n = ptr2+1
                self.count = self.count+tmp_n
                ptr1-=1
            else:
                ptr2-=1
        
    def MergeSort(self,low,mid,high):
        ptr1,ptr2 = low, mid+1

        nums = []
        # if low==0 and high == 4:
        #     print(self.A[low:mid+1],self.A[mid+1:high+1])
        self.check(self.A[low:mid+1],self.A[mid+1:high+1])
        while(ptr1<=mid and ptr2<=high):
            
            if self.A[ptr1]<=self.A[ptr2]:
                nums.append(self.A[ptr1])
                ptr1+=1
            else:
                nums.append(self.A[ptr2])
                ptr2+=1
        if ptr1<=mid:
            nums = nums+self.A[ptr1:mid+1]
        if ptr2<=high:
            nums = nums + self.A[ptr2:high+1]
        index = 0
        for i in range(low,high+1):
            self.A[i] = nums[index]
            index+=1



