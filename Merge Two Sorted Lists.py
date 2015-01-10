# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        p = head
        p1 = l1
        p2 = l2
        while p1!=None or p2!=None:
            if p1==None or p2!=None and p1.val > p2.val:
                p.next = p2
                p = p2
                p2 = p2.next
            else:
                p.next = p1
                p = p1
                p1 = p1.next
        p.next = None
        return head.next
                
        