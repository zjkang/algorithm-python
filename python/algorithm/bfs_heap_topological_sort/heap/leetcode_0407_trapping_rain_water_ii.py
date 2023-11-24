
"""
author: Zhengjian Kang
date: 02/18/2021

残酷群每日一题: 02/17/2021

https://leetcode.com/problems/trapping-rain-water-ii/

407. Trapping Rain Water II

note: BFS + PQ 二维从外向内填充

Given an m x n matrix of positive integers representing the height of each
unit cell in a 2D elevation map, compute the volume of water it is able to
trap after raining.

Example:
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
Return 4.

Constraints:
1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000
"""


class Solution:

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import heapq
        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[False] * n for _ in range(m)]

        queue = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heapq.heappush(queue, (heightMap[i][j], i, j))
                    visited[i][j] = True

        res = 0
        cur = float('-inf')
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        while queue:
            h, x, y = heapq.heappop(queue)
            if h > cur:
                cur = h
            res += cur - h
            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]
                if cx < 0 or cx >= m or cy < 0 or cy >= n:
                    continue
                if visited[cx][cy]:
                    continue
                visited[cx][cy] = True
                heapq.heappush(queue, (heightMap[cx][cy], cx, cy))
        return res
