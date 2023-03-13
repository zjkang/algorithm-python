"""
author: Zhengjian Kang
date: 03/13/2023

https://leetcode.com/problems/evaluate-division/
399. Evaluate Division

note: 构建有向图, search for each query; each query has at most one potential solution
You are given an array of variable pairs equations and an array of real numbers values, 
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            e1 = equations[i][0]
            e2 = equations[i][1]
            graph[e1].append((e2, values[i]))
            graph[e2].append((e1, 1.0 / values[i]))
            
        
        def dfs(src, dest, weight, visited):
            visited.add(src)
            if src == dest:
                return weight
            for neighbor, ratio in graph[src]:
                if neighbor in visited:
                    continue
                val = dfs(neighbor, dest, weight * ratio, visited)
                if val is not None: return val
            return None
        
        res = []
        for q1, q2 in queries:
            if q1 not in graph or q2 not in graph:
                res.append(-1.0)
                continue
            value = dfs(q1, q2, 1.0, set())
            res.append(-1.0 if value is None else value)
        
        return res
