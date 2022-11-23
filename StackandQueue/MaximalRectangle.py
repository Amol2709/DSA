
class Rect(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        self.heights = heights
        self.n = len(self.heights)
        self.pse = self.previousSmaller()
        self.nse = self.nextSmaller()
        #print(self.pse)
        #print(self.nse)
        ans = -sys.maxsize
        for i in range(self.n):
            ans = max(ans,self.heights[i]*(self.nse[i]-self.pse[i]-1))
        return ans
    
    def previousSmaller(self):
        pse = [-1]*self.n
        ptr = 1
        stk = [(self.heights[0],0)]
        
        while(ptr<=self.n-1):
            elem,index = stk[-1]
            if self.heights[ptr]>self.heights[index]:
                pse[ptr]=index
                stk.append((self.heights[ptr],ptr))
            else:
                while(True):
                    if len(stk)==0:
                        stk.append((self.heights[ptr],ptr))
                        break
                    elem,index = stk[-1]
                    
                    if self.heights[ptr]<=self.heights[index]:
                        stk.pop()
                    else:
                        pse[ptr] = index
                        stk.append((self.heights[ptr],ptr))
                        break
            ptr = ptr+1
        return pse
                        
            
    def nextSmaller(self):
        nse = [self.n]*self.n
        ptr = self.n-2
        stk = [(self.heights[self.n-1],self.n-1)]
        
        while(ptr>=0):
            elem,index = stk[-1]
            if self.heights[ptr]>self.heights[index]:
                nse[ptr]=index
                stk.append((self.heights[ptr],ptr))
            else:
                while(True):
                    if len(stk)==0:
                        stk.append((self.heights[ptr],ptr))
                        break
                    elem,index = stk[-1]
                    
                    if self.heights[ptr]<=self.heights[index]:
                        stk.pop()
                    else:
                        nse[ptr] = index
                        stk.append((self.heights[ptr],ptr))
                        break
            ptr = ptr-1
        return nse
                        
            



class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        obj   = Rect()
        prev_arr = []
        r,c = len(matrix),len(matrix[0])
        for i in range(0,c):
            prev_arr.append(int(matrix[0][i]))
        ans = obj.largestRectangleArea(prev_arr)

        for i in range(1,r):
            for j in range(c):
                if int(matrix[i][j])==0:
                    prev_arr[j]=0
                else:
                    prev_arr[j]+=int(matrix[i][j])
            ans = max(ans,obj.largestRectangleArea(prev_arr))
        return ans


















        