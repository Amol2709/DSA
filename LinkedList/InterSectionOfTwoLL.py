# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA==headB:
            return headA
        
        def findLenght(node):
            len_ = 0
            curr = node
            while(curr!=None):
                curr = curr.next
                len_+=1
            return len_
     

        len_a = findLenght(headA)
        len_b = findLenght(headB)

        if len_a>len_b:
            node_number = len_a-len_b
        else:
            node_number = len_b-len_a
            headA,headB = headB,headA
        
        curr = headA
        count = 0
        while(count != node_number):
            count+=1
            curr = curr.next
        curr2 = headB
        if curr == curr2:
            return curr
            
        while(curr!= None and curr2!=None):
            if curr.next == curr2.next:
                return curr.next 
            curr = curr.next 
            curr2 = curr2.next

        return None