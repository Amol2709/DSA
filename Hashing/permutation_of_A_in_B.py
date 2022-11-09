class Solution:
    
    def solve(self, A, B):
        map_a={}
        map_b = {}
        for i in range(len(A)):
            if A[i] in map_a:
                map_a[A[i]]+=1
            else:
                map_a[A[i]]=1
            map_b[A[i]]=0
        n = len(A)
        ans = 0
        for i in range(0,len(B)):
            if B[i] in map_b:
                map_b[B[i]]+=1
            if i>=n:
                if B[i-n] in map_b:
                    map_b[B[i-n]]-=1
            if map_b == map_a:
                ans+=1
            
        return ans
            
            