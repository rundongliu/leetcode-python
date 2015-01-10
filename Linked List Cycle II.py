# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head==None or head.next==None:
            return None
        p1 = head.next
        p2 = head.next.next
        if p2==None:
            return None
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
            if p2 == None:
                return None
            p2 = p2.next
            if p2==None:
                return None
        while head!=p1:
            head = head.next
            p1 = p1.next
        return p1