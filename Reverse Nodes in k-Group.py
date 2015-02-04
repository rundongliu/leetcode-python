# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        front = ListNode(0)
        front.next = head
        p = front
        while p:
            last = p.next
            for i in range(k):
                if not last:
                    return front.next
                last = last.next
            tp = p.next
            tmplast = tp
            for i in range(k):
                tmp = tp.next
                tp.next = last
                last = tp
                tp = tmp
            p.next = last
            p = tmplast
        return front.next
                