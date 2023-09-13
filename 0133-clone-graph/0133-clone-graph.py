"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dict1 = {}
        def help(node):
            if not node:
                return 
            dict1[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in dict1:
                    help(neighbor)
        help(node)
        visited = set()
        def help1(node):
            if not node:
                return None
            temp = dict1[node] 
            visited.add(node)
            for neighbor in node.neighbors:
                if dict1[neighbor] not in temp.neighbors:
                    temp.neighbors.append(dict1[neighbor])
                if neighbor not in visited:
                    help1(neighbor)
            return temp
        return help1(node)


        