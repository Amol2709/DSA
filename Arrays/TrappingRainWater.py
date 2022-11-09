'''
Leetocode: 42
'''

class Solution(object):
    def trap(self, A):
        """
        :type height: List[int]
        :rtype: int
        """
        premax= [A[0]]
        postmax = [0]*len(A)
        postmax[-1]=A[-1]
        for i in range(1,len(A)):
            premax.append(max(premax[i-1],A[i]))
        for j in range(len(A)-2,-1,-1):
            postmax[j]=max((postmax[j+1],A[j]))
        ans=0
        for k in range(0,len(A)):
            ans = ans+ (min(postmax[k],premax[k])-A[k])
        return ans

        