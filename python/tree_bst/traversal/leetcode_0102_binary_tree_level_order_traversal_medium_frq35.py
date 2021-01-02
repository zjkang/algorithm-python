"""
author: Wei Li
date: 10/18/2020

https://leetcode.com/problems/binary-tree-level-order-traversal/

102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Non-recursion
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = collections.deque([root])
        
        while queue:
            size = len(queue)
            
            formed = []
            for _ in range(size):
                node = queue.popleft()
                formed.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(formed)
       
        return result        

# Recursion
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        def helper(root, depth, result):
            if not root:
                return 
            
            if len(result) == depth:
                result.append([])
                
            result[depth].append(root.val)

            helper(root.left, depth + 1, result)
            helper(root.right, depth + 1, result)
                
                
        result = []
        
        helper(root, 0, result)
        return result