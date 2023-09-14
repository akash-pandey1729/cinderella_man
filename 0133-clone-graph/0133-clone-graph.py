"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        dict1 = {}
        def dfs(node):
            if not node:
                return node
            if node in dict1:
                return dict1[node]
            dict1[node] = Node(node.val,[])
            if node.neighbors:
                 dict1[node].neighbors = [dfs(n) for n in node.neighbors]
            return dict1[node]
        return dfs(node)


        