class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        import sys
        temp=[]
        flag = False
        N=len(A)
        for i in range(0,N):
            if A[i]=='1':
                temp.append(-1)
            else:
                temp.append(1)
                flag=True
        if flag==False:
            return []
        
        # kadane ALgo
        curr_sum=0
        max_sum=-sys.maxsize
        Ans=[]
        left,right = 0,0
        for i in range(0,N):
            curr_sum = curr_sum+temp[i]
            if curr_sum>max_sum:
                max_sum = curr_sum
                right=i
                Ans=[left+1,right+1]
            if curr_sum<0:
                curr_sum=0
                left = i+1
        return Ans
        