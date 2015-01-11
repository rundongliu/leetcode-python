# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        front = ListNode(0)
        front.next = head
        p = front
        count = 0
        while p:
            p = p.next
            count += 1
        count -= n
        p = front
        for i in range(count-1):
            p = p.next
        p.next = p.next.next
        return front.next
        