
"""
author: Zhengjian Kang
date: 03/13/2021

残酷群每日一题: 03/10/2021

https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

1786. Number of Restricted Paths From First to Last Node

note: 典型的bfs + PQ + dfs题目，类似word ladder

There is an undirected weighted connected graph. You are given a positive
integer n which denotes that the graph has n nodes labeled from 1 to n, and an
array edges where each edges[i] = [ui, vi, weighti] denotes that there is an
edge between nodes ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk]
such that z0 = start and zk = end and there is an edge between zi and zi+1
where 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path.
Let distanceToLastNode(x) denote the shortest distance of a path between node n
and node x. A restricted path is a path that also satisfies that
distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number
may be too large, return it modulo 109 + 7.

Example 1:
Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],
[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its
distanceToLastNode value in blue. The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5

Example 2:
Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],
[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its
distanceToLastNode value in blue. The only restricted path is 1 --> 3 --> 7.

Constraints:
1 <= n <= 2 * 10^4
n - 1 <= edges.length <= 4 * 10^4
edges[i].length == 3
1 <= ui, vi <= n
ui != vi
1 <= weighti <= 10^5
There is at most one edge between any two nodes.
There is at least one path between any two nodes.
"""


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        self.MOD = 1000000007
        graph = self.build_graph(n, edges)
        shortest_path = self.cal_shortest_path(n, graph)
        if 1 not in shortest_path:
            return 0
        return self.dfs(1, n, shortest_path, graph, {})

    def dfs(self, start, end, shortest_path, graph, memo):
        # memo: # of ways from start to end
        if start == end:
            memo[start] = 1
            return memo[start]
        if start in memo:
            return memo[start]
        total = 0
        for nei, w in graph[start]:
            if shortest_path[nei] < shortest_path[start]:
                total += self.dfs(nei, end, shortest_path, graph, memo)
                total %= self.MOD
        memo[start] = total
        return memo[start]

    def cal_shortest_path(self, n, graph):
        path = defaultdict(int)
        path[n] = 0
        pq = [(0, n)]
        visited = set()
        while pq:
            dist, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            path[node] = dist
            for nei, w in graph[node]:
                if nei in visited:
                    continue
                heapq.heappush(pq, ((dist + w), nei))
        return path

    def build_graph(self, n, edges):
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        return graph
