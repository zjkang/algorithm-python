"""
author: Zhengjian Kang
date: 10/23/2020

残酷群每日一题: 02/13/2021

https://leetcode.com/problems/cheapest-flights-within-k-stops/

787. Cheapest Flights Within K Stops

note: BFS + PQ的典型题目

There are n cities connected by m flights. Each flight starts from city u and
arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the
destination dst, your task is to find the cheapest price from src to dst with
up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
marked blue in the picture.

Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        graph = self.build_graph(n, flights)
        import heapq
        queue = [(0, 0, src)]  # weight, stop, destination
        dequeued = set()
        while queue:
            weight, stop, city = heapq.heappop(queue)
            if city == dst:
                return weight
            if (city, stop) in dequeued: continue
            dequeued.add((city, stop))
            if stop < K + 1: # stop <= K
                for n_dst, n_weight in graph[city]:
                    if (n_dst, stop+1) in dequeued:
                        continue
                    heapq.heappush(queue, (weight+n_weight, stop+1, n_dst))
        return -1

    def build_graph(self, n, flights):
        graph = {i: [] for i in range(n)}
        for src, dst, w in flights:
            graph[src].append((dst, w))
        return graph
