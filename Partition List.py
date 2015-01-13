# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        small = ListNode(0)
        large = ListNode(0)
        p1 = small
        p2 = large
        p = head
        while p!=None:
            if p.val<x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p1.next = large.next
        p2.next = None
        return small.next
        