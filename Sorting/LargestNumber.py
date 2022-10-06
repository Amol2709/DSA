
'''
Given an array A of non-negative integers, arrange them such that they form the largest number.
'''

from functools import cmp_to_key
class Solution(object):
    def compare(self,n1,n2):
        number1 = int(n1+n2)
        number2 = int(n2+n1)
        if number1 >=number2:
            return -1
        else:
            return 1
            
    def largestNumber(self, A):
        A = sorted(list(map(str,A)))
        
        #A.reverse()
        #print(A)
        if A.count('0')==len(A):
            return '0'

        A = sorted(A,key=cmp_to_key(self.compare))
        return "".join(A)
        
        # a = []
        # ptr1,ptr2 = 0,1
        # while(ptr2<len(A)):
        #     if A[ptr2] == A[ptr1]:
        #         ptr2 = ptr2+1
        #     else:
        #         a.append("".join(A[ptr1:ptr2]))
        #         ptr1 = ptr2
        #         ptr2 = ptr2+1
        # a.append("".join(A[ptr1:ptr2]))
        # #print(a)
                
        # for i in range(len(a)-1,0,-1):
        #     if self.compare(a[i-1],a[i])==False:
        #         a[i-1],a[i] = a[i],a[i-1]

        # ans = ""
        # return ans.join(a)
        # #return ans

                
                
            
        