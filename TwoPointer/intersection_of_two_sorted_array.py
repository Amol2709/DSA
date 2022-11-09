class Solution:
    def intersect(self, A, B):
        ptr1,ptr2 = 0,0
        ans = []
        while(ptr1<len(A) and ptr2<len(B)):
            if A[ptr1]==B[ptr2]:
                ans.append(A[ptr1])
                ptr1+=1
                ptr2+=1
            elif A[ptr1]>B[ptr2]:
                ptr2+=1
            else:
                ptr1+=1
        return ans



