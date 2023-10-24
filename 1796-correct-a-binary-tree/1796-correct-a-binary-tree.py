class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        # Queue for BFS. Every element stores [node, parent]
        queue = deque([[root, None]])

        # Traverse Level by Level
        while queue:
            # Nodes in the current level
            n = len(queue)

            # Hash Set to store nodes of the current level
            visited = set()
            print(visited)

            # Traverse all nodes in the current level
            for _ in range(n):
                # Pop the node from the queue
                node, parent = queue.popleft()

                # If node.right is already visited, then the node is defective
                if node.right in visited:
                    # Replace the child of the node's parent with null and return the root
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    return root

                # Add node to visited
                visited.add(node)

                # Add child in queue for traversal in next level
                # They won't get popped in this level because of "n"
                # Add the right child first, so that we can explore right to left
                if node.right:
                    queue.append([node.right, node])
                if node.left:
                    queue.append([node.left, node])