"""
author: Wei Li
date: 10/18/2020

https://leetcode.com/problems/find-duplicate-subtrees/

652. Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200

""" 
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        counter = collections.Counter()
        ans = []
        
        def dfs(root):
            if not root:
                return "#"
            
            serial = "{},{},{}".format(str(root.val), dfs(root.left), dfs(root.right))
            
            counter[serial] += 1
            
            if counter[serial] == 2:
                ans.append(root)
                
            return serial
        
        dfs(root)
        
        return ans