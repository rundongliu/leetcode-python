# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next:
            return head
        p = head
        count = 0
        while p:
            count+=1
            p = p.next
        count = count/2
        p = head
        while count>1:
            p = p.next
            count -= 1
        head2 = p.next
        p.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(head2)
        front = ListNode(0)
        p = front
        while head1 and head2:
            if head1.val<head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
        if head1:
            p.next = head1
        else:
            p.next = head2
        return front.next