"""
author: Zhengjian Kang
date: 10/23/2020

残酷群每日一题: 02/12/2021

https://leetcode.com/problems/network-delay-time/

743. Network Delay Time

note: 经典的priority题目，priority题目所需要考虑的状态是dequeued
一般的搜索题目考虑的状态是
no visit, visiting, visited
enqueued -> visiting, visited
dequeued -> visited

There are N network nodes, labelled 1 to N.
Given times, a list of travel times as directed edges times[i] = (u, v, w),
where u is the source node, v is the target node, and w is the time it takes
for a signal to travel from source to target.
Now, we send a signal from a certain node K. How long will it take for all
nodes to receive the signal? If it is impossible, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = self.build_graph(N, times)
        import heapq
        queue = [(0, K)]
        dequeued = set()
        while queue:
            weight, node = heapq.heappop(queue)
            dequeued.add(node)
            if len(dequeued) == N:
                return weight
            for n_n, n_w in graph[node]:
                if n_n in dequeued:
                    continue
                heapq.heappush(queue, (n_w+weight, n_n))
        return -1

    def build_graph(self, N, times):
        graph = {i+1: [] for i in range(N)}
        for u, v, w in times:
            graph[u].append((v, w))
        return graph
