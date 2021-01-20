"""
author: Zhengjian Kang
date: 10/19/2020

https://leetcode.com/problems/is-graph-bipartite/

785. Is Graph Bipartite?

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two
independent subsets A and B such that every edge in the graph has one node in
A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for
which the edge between nodes i and j exists.  Each node is an integer between 0
and graph.length - 1.  There are no self edges or parallel edges: graph[i] does
not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
"""


from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        for i in range(len(graph)):
            if i not in visited:
                if not self.bfs(i, graph, visited):
                    return False
        return True

    def bfs(self, cur_node, graph, visited):
        queue = deque([cur_node])
        visited.add(cur_node)
        mapping = {cur_node: 0}  # color: 0 or 1
        while queue:
            head = queue.popleft()
            color = mapping[head]
            for n in graph[head]:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)
                    mapping[n] = 0 if color == 1 else 1
                elif mapping[n] == color:
                    return False
        return True
