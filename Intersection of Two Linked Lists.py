# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        countA = 0
        p = headA
        while p!=None:
            p = p.next
            countA += 1
        countB = 0
        p = headB
        while p!=None:
            p = p.next
            countB += 1
        if countA>countB:
            for i in range(countA-countB):
                headA = headA.next
        else:
            for i in range(countB-countA):
                headB = headB.next
        while headA!=headB:
            headA = headA.next
            headB = headB.next
        return headA
        