class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        self.ans = 0
        self.n = len(s)
        self.dp = [-1]*self.n
        return self.myFunc(0)
    def myFunc(self,index):
        if index>=self.n:
            return 1
        if self.dp[index]!=-1:
            return self.dp[index]
        if self.s[index]=='0':
            self.dp[index]=0
            return 0
        cut = 0
        for i in range(index,self.n):
            if int(self.s[index])!=0  and 1<=int(self.s[index:i+1])<=26:
                cut = cut+self.myFunc(i+1)
        self.dp[index]=cut
        return cut
                
        