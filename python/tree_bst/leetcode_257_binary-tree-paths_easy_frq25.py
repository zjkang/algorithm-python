"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/binary-tree-paths/

257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# Non-recursion
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        queue = collections.deque([(root, [str(root.val)])])
        ans = []
        while queue:
            node, path = queue.popleft()
            
            if not node.left and not node.right:
                ans.append("->".join(path[:]))
            
            if node.left:
                queue.append((node.left, path + [str(node.left.val)]))
            
            if node.right:
                queue.append((node.right, path + [str(node.right.val)]))
                
        return ans       
            
# Recursion
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root, formed, ans):
            if not root:
                return
            
            formed.append(str(root.val))
            if not root.left and not root.right:
                ans.append("->".join(formed[:]))
            else:    
                dfs(root.left, formed, ans)
                dfs(root.right, formed, ans)
            formed.pop()
            
        ans = []
        dfs(root, [], ans)
        
        return ans