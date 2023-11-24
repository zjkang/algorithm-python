
"""
author: Zhengjian Kang
date: 03/12/2021

残酷群每日一题: 03/09/2021

https://leetcode.com/problems/count-pairs-of-nodes/

1782. Count Pairs Of Nodes

note: 把点的问题转换成边的问题，考虑two pointers解决，然后去重

You are given an undirected graph represented by an integer n, which is
the number of nodes, and edges, where edges[i] = [ui, vi] which indicates
that there is an undirected edge between ui and vi. You are also given an
integer array queries.

The answer to the jth query is the number of pairs of nodes (a, b) that satisfy
the following conditions:
a < b
cnt is strictly greater than queries[j], where cnt is the number of edges
incident to a or b.
Return an array answers such that answers.length == queries.length and
answers[j] is the answer of the jth query.

Note that there can be repeated edges.


Example 1:
Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
Output: [6,5]
Explanation: The number of edges incident to at least one of each pair is
shown above.

Example 2:
Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]],
queries = [1,2,3,4,5]
Output: [10,10,9,8,6]

Constraints:
2 <= n <= 2 * 10^4
1 <= edges.length <= 10^5
1 <= ui, vi <= n
ui != vi
1 <= queries.length <= 20
0 <= queries[j] < edges.length
"""


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        count = {i: 0 for i in range(1, n+1)}
        edge_count = defaultdict(int)
        for u, v in edges:
            if u > v:
                u, v = v, u
            count[u] += 1
            count[v] += 1
            edge_count[(u, v)] += 1

        count2 = [v for k, v in count.items()]
        count2.sort()

        res = []
        for q in queries:
            i, j = 0, len(count2)-1
            total = 0
            while i < j:
                if count2[i] + count2[j] <= q:
                    i += 1
                else:
                    total += j - i
                    j -= 1
            for (u, v), c in edge_count.items():
                if count[u] + count[v] > q and count[u] + count[v] - c <= q:
                    total -= 1
            res.append(total)

        return res
