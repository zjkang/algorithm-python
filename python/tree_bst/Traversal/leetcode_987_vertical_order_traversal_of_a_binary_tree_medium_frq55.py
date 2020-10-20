"""
author: Wei Li
date: 10/18/2020

https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

987. Vertical Order Traversal of a Binary Tree

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.


Example 1:
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
"""
# Non-recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        node_list = []
        
        def bfs(root):
            queue = collections.deque([(root, 0, 0)])
            while queue:
                size = len(queue)

                for _ in range(size):
                    node, row, column = queue.popleft()
                    node_list.append((column, row, node.val))

                    if node.left:
                        queue.append((node.left, row + 1, column - 1))

                    if node.right:
                        queue.append((node.right, row + 1, column + 1))
         
        bfs(root)
        
        node_list.sort()
        ret = OrderedDict()
        
        for column, row, value in node_list:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]
        
        return ret.values()
# DFS        
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def DFS(node, row, column):
            if node is not None:
                node_list.append((column, row, node.val))
                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        # step 1). construct the node list, with the coordinates
        DFS(root, 0, 0)

        # step 2). sort the node list globally, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results grouped by the column index
        ret = []
        curr_column_index = node_list[0][0]
        curr_column = []
        for column, row, value in node_list:
            if column == curr_column_index:
                curr_column.append(value)
            else:
                # end of a column, and start the next column
                ret.append(curr_column)
                curr_column_index = column
                curr_column = [value]
        # add the last column
        ret.append(curr_column)

        return ret        
        
        
     