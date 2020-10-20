"""
author: Zhengjian Kang
date: 10/12/2020

https://leetcode.com/problems/course-schedule/

207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 
Constraints:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""


# topo sort
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i: 0 for i in range(numCourses)}
        neighbors = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            indegree[i] += 1
            neighbors[j].append(i)
        from collections import deque
        q = deque()
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for n in neighbors[c]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        return len(res) == numCourses


# dfs
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        def build_graph(numCourses, prerequisites):
            graph = {i: [] for i in range(numCourses)}
            for u, v in prerequisites:
                graph[v].append(u)
            return graph

        def is_cycle(course, graph, visited):
            if visited[course] == 1:
                return False
            if visited[course] == 0:
                return True
            visited[course] = 0
            for i in graph[course]:
                if is_cycle(i, graph, visited):
                    return True
            visited[course] = 1
            return False

        graph = build_graph(numCourses, prerequisites)
        # -1: not visit; 0: visiting; 1: visited
        visited = [-1] * numCourses
        for i in range(numCourses):
            if visited[i] == -1 and is_cycle(i, graph, visited):
                return False
        return True
