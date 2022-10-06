'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.
'''



import sys
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.n = len(s)
        self.s = s
        self.dp=[-1]*self.n 
        return self.myFunc(0)
    def myFunc(self,index):
        if index==self.n-1:
            return 0
        if self.dp[index]!=-1:
            return self.dp[index]
        if self.isPallindrome(self.s[index:self.n]):
            self.dp[index]=0
            return 0
        cut = sys.maxsize
        for i in range(index,self.n):
            if self.isPallindrome(self.s[index:i+1]):
                cut = min(cut,1+self.myFunc(i+1))
        self.dp[index]= cut
        return cut
                
        
        
    def isPallindrome(self,word):
        if word == word[::-1]:
            return True
        return False
    
        