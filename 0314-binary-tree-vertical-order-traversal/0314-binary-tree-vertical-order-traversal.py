# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_dict = defaultdict(list)
        def helper(node, pos, depth):
            if not node:
                return 0
            node_dict[pos].append((depth, node.val))
            helper(node.left, pos-1, depth+1)
            helper(node.right, pos+1, depth+1)
        helper(root, 0, 0)
        ans = []
        keys = list(node_dict.keys())
        keys.sort()
        for key in keys:
            node_dict[key].sort(key = lambda x:x[0])
            temp = []
            for _,v in node_dict[key]:
                temp.append(v)
            ans.append(temp[:])
        return ans

            
        
        
        