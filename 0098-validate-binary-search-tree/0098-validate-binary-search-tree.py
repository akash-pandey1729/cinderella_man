class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # Use maximal system integer to represent infinity
        INF = sys.maxsize
        
        def helper(node, lower, upper):
            
            if not node:
				# empty node or empty tree
                return True
            
            if lower < node.val < upper:
				# check if all tree nodes follow BST rule
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
            
            else:
				# early reject when we find violation
                return False
            
        # ----------------------------------
        
        return helper( node=root, lower=-INF, upper=INF )