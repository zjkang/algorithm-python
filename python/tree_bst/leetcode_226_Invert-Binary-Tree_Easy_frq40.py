"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/invert-binary-tree/

226. Invert Binary Tree
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""
# Non-recursion
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        queue = collections.deque([(root, root.left, root.right)])
        while queue:
            node, left, right = queue.popleft()
            
            node.left = right
            node.right = left
            
            if right:
                queue.append((right, right.left, right.right))
            
            if left:
                queue.append((left, left.left, left.right))
       
        return root

# Recursion
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return
            
            left = helper(root.left)
            right = helper(root.right)
            
            root.left = right
            root.right = left
            
            return root
        
        return helper(root)