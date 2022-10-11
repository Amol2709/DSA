class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        map_={}
        ans = 0
        

        # for First element
        curr_xor = A[0]
        map_[curr_xor]=1
        if curr_xor==B:
            ans +=1
        
        for i in range(1,len(A)):
            curr_xor = curr_xor ^ A[i]
            if curr_xor == B:
                ans = ans+1
            
            if curr_xor ^ B in map_:
                ans = ans+map_[curr_xor^B]
                
                
            if curr_xor in map_:
                map_[curr_xor]+=1
            else:
                map_[curr_xor]=1
        return ans
                
            
            
            
                
