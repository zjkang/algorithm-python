"""
author: Wei Li
date: 10/18/2020

https://leetcode.com/problems/binary-tree-preorder-traversal/

144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Example 5:
Input: root = [1,null,2]
Output: [1,2]
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        
        self.addNode(root, result)
        return result

        
    def addNode(self, root, result):
        if root is not None:
            result.append(root.val)
        
        if root and root.left:
            self.addNode(root.left, result)
            
        if root and root.right:
            self.addNode(root.right, result)
            
        return result   

# Non-recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        
        return result