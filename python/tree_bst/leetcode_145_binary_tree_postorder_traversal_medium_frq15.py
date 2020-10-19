"""
author: Wei Li
date: 10/18/2020

https://leetcode.com/problems/binary-tree-postorder-traversal/

145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [2,1]
 
Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:

Recursive solution is trivial, could you do it iteratively?
"""
# Recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        
        self.addNode(root, result)
        return result
    
    def addNode(self, root: TreeNode, result: List[int]):
        if not root:
            return 

        self.addNode(root.left, result)
        self.addNode(root.right, result)
        result.append(root.val)

# Non-recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        
        stack = [root,]
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
                
        return result[::-1]   