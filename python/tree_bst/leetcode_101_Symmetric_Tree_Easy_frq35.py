"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/symmetric-tree/

101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Follow up: Solve it both recursively and iteratively.
"""
# Non-recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:    
        if not root:
            return True
        
        queue = collections.deque([root.left, root.right])
        
        while queue:
            left = queue.popleft()
            right = queue.pop()
            
            if not left and not right:
                continue
            
            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            queue.appendleft(left.left)
            queue.append(right.right)
            
            queue.appendleft(left.right)
            queue.append(right.left)

        return True         

# Recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:      
        def helper(node, mirror):
            if not node and not mirror:
                return True
            
            if not node or not mirror:
                return False
            
            
            left = helper(node.left, mirror.right)
            right = helper(node.right, mirror.left)
            
            return node.val == mirror.val and left and right
        
        return helper(root, root)