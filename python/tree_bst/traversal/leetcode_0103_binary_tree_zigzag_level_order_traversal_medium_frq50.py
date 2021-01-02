"""
author: Wei Li
date: 10/18/2020

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3 
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# Non-recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([(root, 0)])
        result = []
        
        while queue:
            size = len(queue)
            
            formed = collections.deque()
            for _ in range(size):
                node, level = queue.popleft()
                
                if level % 2 == 0:
                    formed.append(node.val)
                else:
                    formed.appendleft(node.val)
                
                if node.left:
                    queue.append((node.left, level + 1))
                    
                if node.right:
                    queue.append((node.right, level + 1))
                    
            
            result.append(formed)
        
        return result
        
# Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        def helper(root, level):
            if not root:
                return
            
            if level == len(ans):
                ans.append(deque())
            
            if level % 2 == 0:
                ans[level].append(root.val)
            else:
                ans[level].appendleft(root.val)
                
            helper(root.left, level + 1)
            helper(root.right, level + 1)
        
        ans = []
        helper(root, 0)
        
        return ans