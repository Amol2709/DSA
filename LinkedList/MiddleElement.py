# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def solve(self, A):

        n = 0
        curr = A
        while(curr!=None):
            curr = curr.next
            n = n+1
        
        slow,fast = A,A

        while(slow!=None and fast.next!=None and fast.next.next!=None):
            slow = slow.next
            fast = fast.next.next
        if n%2!=0:
            return slow.val
        else:
            return slow.next.val 





# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slowPtr, fastPtr = head,head
        while(fastPtr!=None and slowPtr!=None and fastPtr.next!=None ):
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
        return slowPtr