# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        front = ListNode(0)
        front.next = head
        p1 = front
        while p1!=None:
            p2 = p1.next
            while p2!=None and p2.next!=None and p2.val == p2.next.val:
                p2 = p2.next
            p1.next = p2
            p1 = p2
        return front.next
        