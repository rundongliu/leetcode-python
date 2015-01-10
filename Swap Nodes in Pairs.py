# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        front = ListNode(0)
        front.next = head
        p = front
        while True:
            p1=p.next
            if p1==None:
                break
            p2=p1.next
            if p2==None:
                break
            temp = p2.next
            p.next = p2
            p2.next = p1
            p1.next = temp
            p = p1
        return front.next
        