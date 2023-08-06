class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            nonlocal k
            if root==None:
                return None
            left=inorder(root.left)
            if left!=None:
                return left
            k-=1
            if k==0:
                return root.val
            return inorder(root.right)
        return inorder(root)