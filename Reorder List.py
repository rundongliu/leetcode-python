# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        front = ListNode(0)
        count = 0
        p1 = head
        while p1:
            count += 1
            p1 = p1.next
        if count<=2:
            return head
        count = (count-1)/2
        p2 = head
        while count:
            p2 = p2.next
            count -= 1
        tmp = p2.next
        p2.next = None
        p2 = tmp
        last = None
        while p2:
            tmp = p2.next
            p2.next = last
            last = p2
            p2 = tmp
        front.next = last
        p1 = head
        p2 = front.next
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
        return head