"""
author: Zhengjian Kang
date: 10/23/2020

https://leetcode.com/problems/tree-diameter/

1245. Tree Diameter

Given an undirected tree, return its diameter: the number of edges in a
longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a
bidirectional edge between nodes u and v.  Each node has labels in the
set {0, 1, ..., edges.length}.

Example 1:
Input: edges = [[0,1],[0,2]]
Output: 2
Explanation:
A longest path of the tree is the path 1 - 0 - 2.

Example 2:
Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation:
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.

Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
"""


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = self.build_graph(edges)
        self.res = 0
        start = edges[0][0]
        visited = set()
        self.dfs(graph, start, visited)
        return self.res - 1

    def build_graph(self, edges):
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def dfs(self, graph, start, visited):
        # return the longest length rooted with start node
        visited.add(start)
        first, second = 0, 0
        for n in graph[start]:
            if n not in visited:
                length = self.dfs(graph, n, visited)
                if length > first:
                    second = first
                    first = length
                elif length > second:
                    second = length
        root_len = 1 + first
        total_len = 1 + first + second
        self.res = max(self.res, total_len)
        return root_len
