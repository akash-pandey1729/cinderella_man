# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict1 = defaultdict(int)
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            dict1[root.val]+=1
            inorder(root.right)
        inorder(root)
        _max = max(list(dict1.values()))
        ans = []
        for key in dict1:
            if dict1[key]==_max:
                ans.append(key)
        return ans

        