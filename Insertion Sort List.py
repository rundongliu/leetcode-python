# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head==None:
            return None
        front = ListNode(0)
        front.next = head
        p = head
        while p.next:
            if p.next.val>p.val:
                p = p.next
                continue
            tp = front
            while tp.next!=None and tp.next.val<p.next.val:
                tp = tp.next
            current = p.next
            p.next = p.next.next
            tmp = tp.next
            tp.next = current
            current.next = tmp
        return front.next