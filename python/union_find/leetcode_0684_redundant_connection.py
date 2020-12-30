"""
author: Zhengjian Kang
date: 10/11/2020

https://leetcode.com/problems/redundant-connection/

684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.
The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.
Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""


# union-find soltuion
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        n = len(edges)
        uf = UnionFind(n+1)
        for u, v in edges:
            if uf.find(u) == uf.find(v):
                return [u, v]
            else:
                uf.union(u, v)
        return []


# node starts from 1 to N
class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n

    def union(self, a, b):
        r_a = self.find(a)
        r_b = self.find(b)
        if r_a != r_b:
            if self.rank[r_a] < self.rank[r_b]:
                self.parent[r_a] = r_b
            else:
                if self.rank[r_a] == self.rank[r_b]:
                    self.rank[r_a] += 1
                self.parent[r_b] = r_a

    def find(self, a):
        path = []
        while self.parent[a] != -1:
            path.append(a)
            a = self.parent[a]
        for p in path:
            self.parent[p] = a
        return a


# dfs solution: find cycle
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []

        graph = {}
        for idx, (u, v) in enumerate(edges):
            graph[(u, v)] = idx+1
            graph[(v, u)] = idx+1

        visited = set()
        path = []
        if (not self.find_cycle(edges[0][0], path, visited, -1, graph, len(edges))):
            return []

        # find the largest index in the cycle
        large_index = -1
        res_start, res_end = -1, -1
        for i in range(len(path)):
            u, v = path[i], path[(i+1) % len(path)]
            if graph[(u, v)] > large_index:
                large_index = graph[(u, v)]
                res_start = u
                res_end = v
        if res_start > res_end:
            res_start, res_end = res_end, res_start
        return [res_start, res_end]

    def find_cycle(self, cur, path, visited, prev, graph, n):
        # find the cycle path after removing extra nodes
        if cur in visited:
            while path and path[0] != cur:
                path.pop(0)
            return True

        visited.add(cur)
        path.append(cur)

        for nei in range(1, n+1):
            if nei == cur or nei == prev or (cur, nei) not in graph:
                continue
            if self.find_cycle(nei, path, visited, cur, graph, n):
                return True

        visited.remove(cur)
        path.pop()
        return False
