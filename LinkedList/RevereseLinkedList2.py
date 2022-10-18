# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    def reverseBetween(self, A, B, C):
        def reverse(node):
            stk = []

            while(node!=None):
                stk.append(node)
                node = node.next 

            head = stk.pop()
            curr = head
            while(len(stk)!=0):
                curr.next = stk.pop()
                curr = curr.next 
            curr.next = None
            return head
        if A.next == None:
            return A
        if B==C:
            return A
        
        curr,flag,prev_node =  A, True, None
        count = 1
        while(curr!=None):
            if count  == B:
                flag = False
                start_node = curr
              
                count  = count+1
                break
            prev_node = curr 
            curr = curr.next
            count  = count+1
  
        
        curr,flag =  curr.next, True 
        
        while(curr!=None):
            if count == C:
                flag = False
                last_node = curr
                next_node = curr.next
                break
            curr = curr.next
            count = count+1
     
        if prev_node!=None:
            prev_node.next = None
        last_node.next = None
        head=reverse(start_node)
        if prev_node!=None:
            prev_node.next  = head 
        start_node.next = next_node
        if prev_node!=None:
            return A
        return head
        
        
        


