# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        dic = {}
        return self.getnode(node,dic)
    def getnode(self,node,dic):
        if not node:
            return node
        if node in dic:
            return dic[node]
        newnode = UndirectedGraphNode(node.label)
        dic[node] = newnode
        for x in node.neighbors:
            newnode.neighbors.append(self.getnode(x,dic))
        return newnode
        