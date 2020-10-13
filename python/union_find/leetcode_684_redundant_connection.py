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
