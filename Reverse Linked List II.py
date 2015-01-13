# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        front_node = ListNode(0)
        front_node.next = head
        first = front_node
        count = 1
        while count<m:
            first = first.next
            count += 1
        last = first
        while count<=n+1:
            last = last.next
            count += 1
        p = first.next
        for i in range(n-m+1):
            next_p = p.next
            p.next = last
            last = p
            p = next_p
        first.next = last
        return front_node.next