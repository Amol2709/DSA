
class TrieNode():
    def __init__(self):
        self.arr = [None]*26
        self.isend  = False
        self.count  = 0


        


 


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==1:
            return strs[0]
        self.n = len(strs)

        root = TrieNode()
        ### Insert ###
        for word in strs:
            currNode = root
            for elem in word:
                if currNode.arr[ord(elem)-97]==None:
                    newNode =  TrieNode()
                    currNode.arr[ord(elem)-97] = newNode
                    currNode = currNode.arr[ord(elem)-97]
                    currNode.count+=1
                else:
                    currNode = currNode.arr[ord(elem)-97]
                    currNode.count+=1
            currNode.isend = True
            
        
        
        ans = ""
        currNode = root
        word = strs[0]
        for i in range(len(word)):
            if currNode.arr[ord(word[i])-97]!=None:
                currNode = currNode.arr[ord(word[i])-97]
                if currNode.count == self.n:
                    ans = ans+word[i]
                else:
                    break
            else:
                break
        return ans

        
        return ans
        
        




