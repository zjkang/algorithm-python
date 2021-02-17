
"""
author: Zhengjian Kang
date: 02/17/2021

残酷群每日一题: 02/14/2021

https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

1761. Minimum Degree of a Connected Trio in a Graph

note: 没有什么特别的解法，暴力求解

You are given an undirected graph. You are given an integer n which is the
number of nodes in the graph and an array edges, where each edges[i] = [ui, vi]
indicates that there is an undirected edge between ui and vi.

A connected trio is a set of three nodes where there is an edge between every
pair of them.
The degree of a connected trio is the number of edges where one endpoint is
in the trio, and the other is not.
Return the minimum degree of a connected trio in the graph, or -1 if the graph
has no connected trios.

Example 1:
Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
Output: 3
Explanation: There is exactly one trio, which is [1,2,3]. The edges that
form its degree are bolded in the figure above.

Example 2:
Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
Output: 0
Explanation: There are exactly three trios:
1) [1,4,3] with degree 0.
2) [2,5,6] with degree 2.
3) [5,6,7] with degree 2.

Constraints:
2 <= n <= 400
edges[i].length == 2
1 <= edges.length <= n * (n-1) / 2
1 <= ui, vi <= n
ui != vi
There are no repeated edges.
"""


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph, count_map = self.build_graph(n, edges)
        res = float('inf')

        for i in range(1, n+1):
            if count_map[i] < 2:
                continue
            for j in range(i+1, n+1):
                if count_map[j] < 2:
                    continue
                for k in range(j+1, n+1):
                    if count_map[k] < 2:
                        continue
                    if graph[i][j] and graph[i][k] and graph[j][k]:
                        res = min(res, count_map[i] +
                                  count_map[j] + count_map[k] - 6)

        return -1 if res == float('inf') else res

    def build_graph(self, n, edges):
        graph = [[0] * (n+1) for _ in range(n+1)]
        count_map = [0] * (n+1)
        for u, v in edges:
            graph[u][v] = 1
            graph[v][u] = 1
            count_map[u] += 1
            count_map[v] += 1
        return graph, count_map
