
'''
Tom and Harry are given N numbers, with which they play a game as a team.

Initially, Tom chooses a particular number P from the N numbers,
 and he takes away all the numbers that are equal to P.

Next, Harry chooses a different number Q, different from what Tom chose, 
and takes away all the numbers equal to Q from the remaining N numbers.

They win the game if they can take all 
the numbers by doing the above operation once and
 if each of them has the same amount of numbers towards the end.

If they win, return the string "WIN", else return "LOSE".


'''


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
