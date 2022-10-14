class Solution:
    def solve(self, A):
        map = {'}':'{',')':'(',']':'['}
        open_={'{','[','('}
        stk = []

        for i in range(len(A)):
            if A[i] in open_:
                stk.append(A[i])
            else:
                if len(stk)==0:
                    return 0
                open_brace = stk.pop()
                if map[A[i]]!=open_brace:
                    return 0
        if len(stk)!=0:
            return 0
        return 1

