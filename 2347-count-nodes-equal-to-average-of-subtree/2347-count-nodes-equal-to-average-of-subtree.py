# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        dict_count = defaultdict(int)
        dict_sum = defaultdict(int)
        def funcCount(root):
            if not root:
                return 0
            left = funcCount(root.left)
            right = funcCount(root.right)
            dict_count[root] = left+right +1
            return  dict_count[root]

        def funcSum(root):
            if not root:
                return 0
            left =  funcSum(root.left)
            right = funcSum(root.right)
            dict_sum[root] = left+right + root.val
            return dict_sum[root]
        funcCount(root)
        funcSum(root)
        # print(dict_count)
        # print(dict_sum)
        ans = 0
        for key in dict_count:
            if dict_sum[key]//dict_count[key] == key.val:
                ans+=1
        return ans


        