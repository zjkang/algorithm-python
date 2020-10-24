"""
author: Wei Li
date: 10/18/2020

https://leetcode.com/problems/delete-nodes-and-return-forest/

1110. Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.

""" 
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        
        def helper(root, to_delete):
            if not root:
                return None
  
            root.left = helper(root.left, to_delete)
            root.right = helper(root.right, to_delete)
            
            if root.val in to_delete:
                if root.left:
                    self.ans.append(root.left)
                
                if root.right:
                    self.ans.append(root.right)
                
                return None
            
            return root
               
        helper(root, to_delete)
        
        if root.val not in to_delete:
            self.ans.append(root) 
        
            
        return self.ans    