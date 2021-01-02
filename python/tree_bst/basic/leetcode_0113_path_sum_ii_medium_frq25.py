"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/path-sum-ii/

113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Non-recursion
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([(root, sum, [root.val])])
        
        ans = []
        while queue:
            node, val_left, path = queue.popleft()
            
            if not node.left and not node.right and node.val == val_left:
                ans.append(path[:])
                
            if node.left:
                queue.append((node.left, val_left - node.val, path + [node.left.val]))
            
            if node.right:
                queue.append((node.right, val_left - node.val, path + [node.right.val]))
        
        return ans     

# Recursion
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root, sum, formed, ans):
            if not root:
                return
            
            formed.append(root.val)
            
            if not root.left and not root.right and sum == root.val:
                ans.append(formed[:])
            else:    
                dfs(root.left, sum - root.val, formed, ans)
                dfs(root.right, sum - root.val, formed, ans)
            formed.pop()
        
        ans = []
        dfs(root, sum, [], ans)
        
        return ans