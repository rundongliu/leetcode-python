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
        p = front
        front.next = head
        tp = p.next
        while tp:
            current=tp.val
            count = 0
            while tp and tp.val==current:
                count += 1
                tp = tp.next
            if count==1:
                p = p.next
                tp = p.next
            else:
                p.next = tp
        return front.next