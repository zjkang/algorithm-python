"""
author: Zhengjian Kang
date: 10/23/2020

https://leetcode.com/problems/critical-connections-in-a-network/

1192. Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected
server-to-server connections forming a network where connections[i] = [a, b]
represents a connection between servers a and b. Any server can reach any other
server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server
unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = {i: set() for i in range(n)}
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)

        jumps = [0] * n
        self.res = []
        self.dfs(0, -1, 0, graph, jumps)
        return self.res

    def dfs(self, cur, par, level, graph, jumps):
        if jumps[cur] > 0:
            return jumps[cur]
        level += 1
        jumps[cur] = level
        for n in graph[cur]:
            if n == par:
                continue
            jumps[cur] = min(jumps[cur], self.dfs(n, cur, level, graph, jumps))
        if jumps[cur] == level and par != -1:
            self.res.append([cur, par])
        return jumps[cur]
