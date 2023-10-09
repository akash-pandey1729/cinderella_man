# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def postorder(root):
            if not root:
                return 
            postorder(root.left)
            postorder(root.right)
            res.append(str(root.val))
        postorder(root)
        temp = ",".join(res)
        return temp


        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        postorder = [int(i) for i in data.split(",") if i.isnumeric()] #[1, 3, 2]
        inorder = sorted(postorder) #[1, 2, 3]
        # tree = [2,1,3]
        def getTree(inorder, postorder):
            if postorder and inorder:
                # print(inorder, postorder)
                temp = postorder.pop()
                root = TreeNode(temp)
                root.right = getTree(inorder[inorder.index(temp)+1:], postorder)
                root.left = getTree(inorder[0:inorder.index(temp)], postorder)
                return root
        return getTree(inorder, postorder)
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans