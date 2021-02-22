"""
author: Zhengjian Kang
date: 02/21/2021

残酷群每日一题: 02/20/2021

https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

1368. Minimum Cost to Make at Least One Valid Path in a Grid

note: BFS + PQ常规做法

Given a m x n grid. Each cell of the grid has a sign pointing to the next
cell you should visit if you are currently in this cell. The sign
of grid[i][j] can be:
1 which means go to the cell to the right. (i.e go from grid[i][j]
to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j]
to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some invalid signs on the cells of the grid which
points outside the grid.

You will initially start at the upper left cell (0,0). A valid path in the
grid is a path which starts from the upper left cell (0,0) and ends at the
bottom-right cell (m - 1, n - 1) following the signs on the grid.
The valid path doesn't have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a
cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Example 1:
Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3)
change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) -->
(1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) -->
(2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

Example 2:
Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).

Example 3:
Input: grid = [[1,2],[4,3]]
Output: 1

Example 4:
Input: grid = [[2,2,2],[2,2,2]]
Output: 3

Example 5:
Input: grid = [[4]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
"""


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = [(0, 0, 0)]  # cost, x, y
        visited = [[False] * n for _ in range(m)]

        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        mapping = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        while queue:
            cost, x, y = heapq.heappop(queue)
            if x == m-1 and y == n-1:
                return cost
            if visited[x][y]:
                continue
            visited[x][y] = True
            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]
                if cx < 0 or cx >= m or cy < 0 or cy >= n:
                    continue
                if visited[cx][cy]:
                    continue
                if mapping[grid[x][y]] == (dx[i], dy[i]):
                    extra = 0
                else:
                    extra = 1
                heapq.heappush(queue, (cost + extra, cx, cy))

        return -1
