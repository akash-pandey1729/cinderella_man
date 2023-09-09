class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        lh=self.leftHeight(root)
        rh=self.rightHeight(root)
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
    
    def leftHeight(self,root):
        c=0
        while root!=None:
            c+=1
            root=root.left
        return c
    
    def rightHeight(self,root):
        c=0
        while root!=None:
            c+=1
            root=root.right
        return c