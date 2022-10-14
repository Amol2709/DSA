class Solution:
    def braces(self, A):
        stk = []
        operator = {'+','-','*','/'}
        
        for i in range(len(A)):
            if A[i]==')':
                if len(stk)==1 and stk[0]=='(':
                        return 1
                if len(stk)==2:
                    return 1
                s=set()
                while(True):
                    if stk[-1]=='(':
                        stk.pop()
                        if len(s.intersection(operator))==0:
                            return 1
                        break
                    else:
                        s.add(stk.pop())
            else:
                stk.append(A[i])
        return 0
                    


