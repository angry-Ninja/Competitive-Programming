# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head=curr=ListNode(0)
        
        # curr.next = somthing ==> this joins the complete
        #list in in front of node somthing is pointing
        
        while l1!=None and l2!=None:
            
            if l1.val<=l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        
        if l1!=None:    
            curr.next=l1  #joins complete list at once 
        
        elif l2!=None:
            curr.next=l2   #no neeed to iterate like in merge sort
            
        
        return head.next
