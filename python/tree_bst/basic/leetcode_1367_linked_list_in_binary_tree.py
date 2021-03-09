
"""
author: Zhengjian Kang
date: 03/08/2021

残酷群每日一题: 02/07/2021

https://leetcode.com/problems/linked-list-in-binary-tree/

1367. Linked List in Binary Tree

Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head
correspond to some downward path connected in the binary tree otherwise
return False.

In this context downward path means a path that starts at some node and
goes downwards.

Example 1:
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,
null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.

Example 2:
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,
null,1,3]
Output: true

Example 3:
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,
null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements
of the linked list from head.

Constraints:
The number of nodes in the tree will be in the range [1, 2500].
The number of nodes in the list will be in the range [1, 100].
1 <= Node.val <= 100 for each node in the linked list and binary tree.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        self.list = []
        self.sufix = []
        self.dp = [0] * 2500

        self.preprocess(head)
        return self.dfs(root, 0)

    def dfs(self, root, depth):
        if not root:
            return False
        if depth == 0:
            self.dp[depth] = self.list[0] == root.val
        else:
            j = self.dp[depth-1]
            while j > 0 and self.list[j] != root.val:
                j = self.sufix[j-1]
            self.dp[depth] = j + (self.list[j] == root.val)
        # print(depth, root.val, self.dp[depth])
        if self.dp[depth] == len(self.list):
            return True
        return self.dfs(root.left, depth+1) or self.dfs(root.right, depth+1)

    def preprocess(self, head):
        while head:
            self.list.append(head.val)
            head = head.next
        n = len(self.list)
        self.sufix = [0] * n
        for i in range(1, n):
            j = self.sufix[i-1]
            while j > 0 and self.list[i] != self.list[j]:
                j = self.sufix[j-1]
            self.sufix[i] = j + (self.list[i] == self.list[j])
