# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head:
            return head
        count = 1
        p = head
        while p.next:
            count+=1
            p = p.next
        k = k%count
        if count<=k or k==0:
            return head
        count = count - k-1
        tmp = head
        while count:
            head =  head.next
            count -= 1
        node = head.next
        head.next = None
        p.next = tmp
        return node