# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    def swapPairs(self, A):
        if A==None or A.next ==None:
            return A
        def reversePair(node):
            if node.next!=None:
                tmpNode = node.next
                node.next.next = node
                node.next = None
                return tmpNode
            return node
        curr = A
        node  = A.next.next
        head = reversePair(curr)
        tmpNode = None
        while(node!=None):
            if node.next != None:
                tmpNode = node.next.next
            else:
                tmpNode = None
            curr.next = reversePair(node)
            curr = node
            node = tmpNode

        return head
