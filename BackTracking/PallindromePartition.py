'''
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

'''



class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.s = s
        self.n = len(self.s)
        self.ans=[]
        self.myFunc(0,[])
        return self.ans
    def myFunc(self,index,tmp):
        if index==self.n:
            self.ans.append(tmp)
        for i in range(index,self.n):
            if self.isPallindrome(self.s[index:i+1]):
                self.myFunc(i+1,tmp+[self.s[index:i+1]])
            
            
            
    def isPallindrome(self,curr_str):
        if len(curr_str)<=1:
            return True
        p1,p2 = 0,len(curr_str)-1
        while(p1<p2):
            if curr_str[p1]==curr_str[p2]:
                p1+=1
                p2-=1
            else:
                return False
        return True
                
        
        