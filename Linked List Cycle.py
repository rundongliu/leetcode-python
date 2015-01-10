# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head==None:
            return False
        p2=head.next
        if p2==None or p2.next==None:
            return False
        p1 = head
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
            if p2==None or p1==None or p2.next==None:
                return False
            p2 = p2.next
        return True
        