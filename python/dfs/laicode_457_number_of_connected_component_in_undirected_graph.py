"""
author: Zhengjian Kang
date: 10/08/2020

https://app.laicode.io/app/problem/457

457. Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:

     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""


class Solution(object):
    def countComponents(self, n, edges):
        """
        input: int n, int[][] edges
        return: int
        """
        visited = set()
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = 0
        for i in range(n):
            if i in graph and i not in visited:
                self.dfs(i, graph, visited)
                res += 1
        return res

    def dfs(self, node, graph, visited):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            self.dfs(neighbor, graph, visited)
