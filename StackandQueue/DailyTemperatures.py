class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        nge = [n]*n
        stk = [n-1]
        for i in range(n-2,-1,-1):
            if temperatures[i]>=temperatures[stk[-1]]:
                while(True):
                    if len(stk)==0:
                        nge[i]= n
                        stk.append(i)
                        break
                    if temperatures[i]>=temperatures[stk[-1]]:
                        stk.pop()
                    else:
                        nge[i] = stk[-1]
                        stk.append(i)
                        break
        
            else:
                nge[i] = stk[-1]
                stk.append(i)
        #print(nge)
        ans = []
        for i in range(n):
            if nge[i]==n:
                ans.append(0)
            else:
                ans.append(nge[i]-i)
        return ans
                    
            
