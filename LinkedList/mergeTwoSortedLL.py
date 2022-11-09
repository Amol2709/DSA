# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1==list2==None:
            return list1
        if list1==None:
            return list2
        if list2 == None:
            return list1
        if list1.val<=list2.val:
            head = list1
            ptr1 = head.next
            ptr2 = list2
            curr = head
        else:
            head = list2
            ptr1 = head.next
            ptr2 = list1
            curr = head
            
        while(ptr1 != None and ptr2 != None):
            if ptr1.val<=ptr2.val:
                curr.next = ptr1
                curr= ptr1
                ptr1 = ptr1.next
            else:
                curr.next = ptr2
                curr = ptr2
                ptr2 = ptr2.next
        if ptr1==None and ptr2!=None:
            curr.next = ptr2
        if ptr2==None and ptr1!=None:
            curr.next = ptr1
        return head
