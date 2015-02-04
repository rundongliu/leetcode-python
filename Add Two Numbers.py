# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, p1, p2):
        front = ListNode(0)
        p = front
        carry = 0
        while p1 or p2:
            if not p1:
                a = 0
            else:
                a = p1.val
                p1 = p1.next
            if not p2:
                b = 0
            else:
                b = p2.val
                p2= p2.next
            num = (a+b+carry)
            node = ListNode(num%10)
            carry = num/10
            p.next = node
            p = node
        if carry:
            p.next = ListNode(carry)
        return front.next