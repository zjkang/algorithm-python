'''
author: Zhengjian Kang
date: 05/17/2021

残酷群每日一题: 05/16/2021

https://leetcode.com/problems/find-eventual-safe-states/

802. Find Eventual Safe States

note: 找环问题, 消除dependency，top sort

We start at some node in a directed graph, and every turn, we walk along a directed edge of the graph.
If we reach a terminal node (that is, it has no outgoing directed edges), we stop.

We define a starting node to be safe if we must eventually walk to a terminal node.
More specifically, there is a natural number k, so that we must have stopped at a terminal node
in less than k steps for any choice of where to walk.

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

The directed graph has n nodes with labels from 0 to n - 1, where n is the length of graph. The graph is
given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph, going from node i to node j.

Example 1:
Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.

Example 2:
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
 

Constraints:

n == graph.length
1 <= n <= 10^4
0 <= graph[i].legnth <= n
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 10^4].
'''


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # reverse indegree & outdegree, start from terminal node
        n = len(graph)
        r_graph = {i: set() for i in range(n)}
        indegree = [0] * n
        for idx, neis in enumerate(graph):
            for nei in neis:
                r_graph[nei].add(idx)
                indegree[idx] += 1
        queue = deque([])
        for idx, d in enumerate(indegree):
            if d == 0:
                queue.append(idx)
        
        rets = []
        while queue:
            cur = queue.popleft()
            rets.append(cur)
            for nei in r_graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        rets.sort()
        return rets
