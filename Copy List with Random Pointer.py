# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        front = RandomListNode(0)
        p1 = head
        p2 = front
        dic = {}
        while p1:
            new_node = RandomListNode(p1.label)
            dic[p1] = new_node
            p2.next = new_node
            p2 = p2.next
            p1 = p1.next
        p = front.next
        p1 = head
        p2 = front.next
        while p1:
            if p1.random:
                p2.random = dic[p1.random]
            p1 = p1.next
            p2 = p2.next
        return front.next