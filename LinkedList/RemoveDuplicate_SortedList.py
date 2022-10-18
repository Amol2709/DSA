# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    def deleteDuplicates(self, A):
        head = A
        ptr1,ptr2 = A,A.next
        if ptr2 == None:
            return head



        while(ptr2!=None):
            if ptr2.val == ptr1.val:
                ptr2 = ptr2.next 
            else:
                ptr1.next = ptr2 
                ptr1 = ptr2 
                ptr2 = ptr2.next
        
        ptr1.next = None

        return head
