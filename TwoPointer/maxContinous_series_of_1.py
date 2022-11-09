class Solution:
    def maxone(self, A, B):
        count = 0
        ptr1,ptr2 = 0,0
        max_len = -1
        ans_index = []
        while(ptr2<len(A)):
            if A[ptr2]==0:
                count+=1
            if count>B:
                if max_len<ptr2-ptr1:
                    ans_index=[ptr1,ptr2-1]
                    max_len = ptr2-ptr1
                elif max_len==ptr2-ptr1:
                    if ptr1<ans_index[0]:
                        ans_index=[ptr1,ptr2-1]
                
                while(True):
                    if count<=B:
                        break
                    if A[ptr1]==0:
                        count = count-1
                    ptr1+=1
            

            ptr2+=1
        if ptr2-ptr1>max_len:
            return list(range(ptr1,ptr2))
        
        return list(range(ans_index[0],ans_index[1]+1))