"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/minimum-depth-of-binary-tree/

111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""            
# non Recursion
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque([(root, 1)])
        
        min_depth = sys.maxsize
        while queue:
            size = len(queue)
            
            for _ in range(size):
                node, level = queue.popleft()
                
                if not node.left and not node.right:
                    return level
                    
                if node.left:
                    queue.append((node.left, level + 1))
                
                if node.right:
                    queue.append((node.right, level + 1))
        
        return min_depth

# Recursion
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        self.min_depth = float('inf')
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if not left or not right:
                return left + right + 1
            
         
            return min(left, right) + 1
        
        
        return dfs(root)