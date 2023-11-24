"""
author: Zhengjian Kang
date: 01/17/2021

残酷群每日一题: 01/16/2021; 05/03/2021;

https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

1697. Checking Existence of Edge Length Limited Paths

note: union-find + binary search; 
这道题也是offline querying的专题的题目

An undirected graph of n nodes is defined by edgeList, where edgeList[i] =
[ui, vi, disi] denotes an edge between nodes ui and vi with distance disi.
Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to
determine for each queries[j] whether there is a path between pj and qj
such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and
the jth value of answer is true if there is a path for queries[j] is true,
and false otherwise.

Example 1:
Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]],
queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two
overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is
less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with
distances less than 5, thus we return true for this query.

Example 2:
Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]],
queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.
"""


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.father = [0] * n
        for i in range(n):
            self.father[i] = i

        res = [False] * len(queries)
        for i in range(len(queries)):
            queries[i].append(i)
        edgeList.sort(key=lambda x: x[2])
        queries.sort(key=lambda x: x[2])

        i = 0
        for q in queries:
            while i < len(edgeList) and edgeList[i][2] < q[2]:
                a = edgeList[i][0]
                b = edgeList[i][1]
                if self.find_father(a) != self.find_father(b):
                    self.union(a, b)
                i += 1
            if self.find_father(q[0]) == self.find_father(q[1]):
                res[q[3]] = True
        return res

    def find_father(self, x):
        if self.father[x] != x:
            self.father[x] = self.find_father(self.father[x])
        return self.father[x]

    def union(self, x, y):
        x = self.find_father[x]
        y = self.find_father[y]
        if x < y:
            self.father[y] = x
        else:
            self.father[x] = y
