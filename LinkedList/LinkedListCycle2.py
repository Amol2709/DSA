# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head 
        while(slow!=None and fast!=None and fast.next!=None):
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                break
        if slow == None or fast==None or fast.next == None:
            return None
        #print(slow.val,fast.val)
        slow = head
       
        while(True):
            if slow == fast:
                #print(slow.val,fast.val)
                return slow
            slow = slow.next 
            fast = fast.next

