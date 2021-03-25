
"""
author: Zhengjian Kang
date: 03/25/2021

残酷群每日一题: 01/12/2021

https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

1719. Number Of Ways To Reconstruct A Tree

note: graph no idea

You are given an array pairs, where pairs[i] = [xi, yi], and:

There are no duplicates.
xi < yi
Let ways be the number of rooted trees that satisfy the following conditions:

The tree consists of nodes whose values appeared in pairs.
A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi
is an ancestor of xi.
Note: the tree does not have to be a binary tree.
Two ways are considered to be different if there is at least one node that has
different parents in both ways.

Return:
0 if ways == 0
1 if ways == 1
2 if ways > 1
A rooted tree is a tree that has a single root node, and all edges are
oriented to be outgoing from the root.
An ancestor of a node is any node on the path from the root to that node
(excluding the node itself). The root has no ancestors.

Example 1:
Input: pairs = [[1,2],[2,3]]
Output: 1
Explanation: There is exactly one valid rooted tree, which is shown in the
above figure.

Example 2:
Input: pairs = [[1,2],[2,3],[1,3]]
Output: 2
Explanation: There are multiple valid rooted trees. Three of them are shown
in the above figures.

Example 3:
Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
Output: 0
Explanation: There are no valid rooted trees.

Constraints:
1 <= pairs.length <= 10^5
1 <= xi < yi <= 500
The elements in pairs are unique.
"""


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        flag = 1
        node_set = set()
        relative = defaultdict(list)
        is_relative = {}
        for x, y in pairs:
            node_set.add(x)
            node_set.add(y)
            relative[x].append(y)
            relative[y].append(x)
            is_relative[(x, y)] = True
            is_relative[(y, x)] = True

        nodes = list(node_set)
        nodes.sort(key=lambda x: len(relative[x]))
        # print(nodes)

        root = -1
        for i in range(len(nodes)):
            j = i + 1
            while j < len(nodes) and (nodes[i], nodes[j]) not in is_relative:
                j += 1
            if j < len(nodes):
                for r in relative[nodes[i]]:
                    if r != nodes[j] and (r, nodes[j]) not in is_relative:
                        return 0
                if len(relative[nodes[i]]) == len(relative[nodes[j]]):
                    flag = 2
            else:
                if root == -1:
                    root = nodes[i]
                else:
                    return 0

        return flag
