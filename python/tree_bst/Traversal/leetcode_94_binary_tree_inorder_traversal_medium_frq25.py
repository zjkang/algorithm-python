"""
author: Wei Li
date: 10/18/2020

https://leetcode.com/problems/binary-tree-inorder-traversal/

94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

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
Output: [1,2]
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
Follow up:

Recursive solution is trivial, could you do it iteratively?
"""
# Non-recursion
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
             
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        
        return result
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        
        curr = root
        while curr is not None:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right is not None and prev.right is not curr:
                    prev = prev.right
                
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    result.append(curr.val)
                    curr = curr.right
        return result       

# Recursion
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.addNode(root, result)
        return result
    
    def addNode(self, root, result):
        if root and root.left:
            self.addNode(root.left, result)
            
        if root:
            result.append(root.val)
            
        if root and root.right:
            self.addNode(root.right, result)
            
        return result   


# Kang's solution
def inorder(root):
    stack = []
    push_left(root, stack)
    while stack:
        cur = stack.pop()
        visit(cur.val)
        push_left(cur.right, stack)

def push_left(root, stack):
    while root:
        stack.append(root)
        root = root.left
