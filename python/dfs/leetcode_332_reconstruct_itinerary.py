"""
author: Zhengjian Kang
date: 10/13/2020

https://leetcode.com/problems/reconstruct-itinerary/

332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival
airports [from, to], reconstruct the itinerary in order. All of the tickets
belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that
has the smallest lexical order when read as a single string. For example, the
itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is
["JFK","SFO","ATL","JFK","ATL","SFO"].
But it is larger in lexical order.
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        graph = self.build_graph(tickets)
        self.dfs(graph, "JFK", 0, len(tickets), res)
        return res

    def dfs(self, graph, start, level, depth, res):
        if level == depth:
            res.append(start)
            return True
        if start not in graph or not graph[start]:
            return False

        res.append(start)
        for idx, nei in enumerate(graph[start]):
            graph[start].pop(idx)
            if self.dfs(graph, nei, level + 1, depth, res):
                return True
            graph[start].insert(idx, nei)
        res.pop()
        return False

    def build_graph(self, tickets):
        from collections import defaultdict
        graph = defaultdict(list)
        for s, d in tickets:
            graph[s].append(d)
        for v in graph.values():
            v.sort()
        return graph
