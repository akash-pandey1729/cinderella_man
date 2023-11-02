# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dict1 = {}
        def traverse(root,val):
            if not root:
                return
            else:
                traverse(root.left, val-1)
                if root not in dict1:
                    dict1[root] = val
                traverse(root.right, val+1)
        traverse(root,0)
        dict2 = {}
        def bfs(root):
            stack = []
            stack.append(root)
            while stack:
                t = len(stack)
                for i in range(t):
                    temp = stack.pop(0)
                    if dict1[temp] not in dict2:
                        dict2[dict1[temp]] = [temp.val]
                    else:
                        dict2[dict1[temp]].append(temp.val)
                    if temp.left:
                        stack.append(temp.left)
                    if temp.right:
                        stack.append(temp.right)
        bfs(root)             
        # print(dict2)  
        dict2 = {k: dict2[k] for k in sorted(dict2)}
        # print(dict2) 
        ans = []
        for key in dict2:
            ans.append(dict2[key][:])
        return ans
                    
                
            
        