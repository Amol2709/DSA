class TrieNode():
    def __init__(self):
        self.arr = [None]*26
        self.isend  = False

class Trie(object):

    def __init__(self):
        self.rootNode=TrieNode()
        


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        currNode = self.rootNode
        for elem in word:
            if currNode.arr[ord(elem)-97]==None:
                newNode =  TrieNode()
                currNode.arr[ord(elem)-97] = newNode
                currNode = currNode.arr[ord(elem)-97]
            else:
                currNode = currNode.arr[ord(elem)-97]
        currNode.isend = True


        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        currNode = self.rootNode
        for elem in word:
            if currNode.arr[ord(elem)-97]==None:
                return False 
            else:
                currNode = currNode.arr[ord(elem)-97]
        if currNode.isend:
            return True
        return False

        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        currNode = self.rootNode
        for elem in prefix:
            if currNode.arr[ord(elem)-97]==None:
                return False 
            else:
                currNode = currNode.arr[ord(elem)-97]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)