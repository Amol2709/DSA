class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        _map = {}
        for i in range(len(A)):
            if A[i] in _map:
                _map[A[i]]+=1
            else:
                _map[A[i]]=1
        s = list(set(A))
        if len(s)==2:
            tom,harry = 0,0
            
            tom+=_map[s.pop()]
            harry+=_map[s.pop()]

            if len(s)==0 and tom == harry:
                return 'WIN'
        return 'LOSE'
