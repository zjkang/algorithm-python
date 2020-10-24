"""
author: Zhengjian Kang
date: 10/08/2020

https://app.laicode.io/app/problem/497

497. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether these edges
make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all
edges are undirected, [0, 1] is the same as [1, 0]and thus will not appear
together in edges.
"""


# method 1: connected + (|E|==|V|-1)
class Solution(object):
    def validTree(self, n, edges):
        """
        input: int n, int[][] edges
        return: boolean
        """
        if len(edges) != n-1:
            return False
        visited = set()
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        self.dfs(0, graph, visited)
        # check if the number of node visited == n
        return len(visited) == n

    def dfs(self, node, graph, visited):
        if node in visited:
            return
        if node not in graph:
            return
        visited.add(node)
        for neighbor in graph[node]:
            self.dfs(neighbor, graph, visited)


# method 2: acyclic + (|E|==|V|-1)
class Solution2(object):
    def validTree(self, n, edges):
        """
        input: int n, int[][] edges
        return: boolean
        """
        if len(edges) != n-1:
            return False
        visited = set()
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if i not in visited and self.is_cyclic(i, -1, graph, visited):
                return False
        return True

    def is_cyclic(self, node, prev, graph, visited):
        if node in visited:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor != prev and self.is_cyclic(
                    neighbor, node, graph, visited):
                return True
        return False
