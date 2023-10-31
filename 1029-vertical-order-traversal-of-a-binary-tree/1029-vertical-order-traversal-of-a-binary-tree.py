# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict1 = defaultdict(list)
        dict1[0] = [[0,root.val]]
        dict_node_col = defaultdict(int)
        dict_node_col[root] = 0
        stack = [root]
        row = -1
        while stack:
            row+=1
            n = len(stack)
            for i in range(n):
                node = stack.pop(0)
                if node.left:
                    dict_node_col[node.left] = dict_node_col[node]-1
                    dict1[dict_node_col[node.left]].append([row, node.left.val])
                    stack.append(node.left)
                if node.right:
                    dict_node_col[node.right] = dict_node_col[node]+1
                    dict1[dict_node_col[node.right]].append([row, node.right.val])
                    stack.append(node.right)
                
        keys = []
        for key in dict1.keys():
            keys.append(key)
            dict1[key].sort(key = lambda x:x[1])
            dict1[key].sort(key = lambda x:x[0])
        keys.sort()
        ans = []
        for key in keys:
            ans.append([node[1] for node in  dict1[key]])
        return ans





        