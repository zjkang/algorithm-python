"""
author: Wei Li
date: 10/19/2020

https://leetcode.com/problems/inorder-successor-in-bst-ii/

510. Inorder Successor in BST II

Given a node in a binary search tree, find the in-order successor of that node in the BST.

If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 

Follow up:

Could you solve it without looking up any of the node's values?

"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
                
            return node
        
        while node.parent and node == node.parent.right:
            node = node.parent
        
        return node.parent