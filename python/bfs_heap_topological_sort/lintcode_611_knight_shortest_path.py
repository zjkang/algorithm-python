"""
author: Wei Li
date: 10/10/2020

https://www.lintcode.com/problem/knight-shortest-path/description?_from=ladder&&fromId=161

611. Knight Shortest Path

Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.

样例
Example 1:
Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]

Example 2:
Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output:-1
说明
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
注意事项
source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.
"""
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortestPath(self, grid, source, destination):
        if not source or not destination:
            return 0

        M = len(grid)
        N = len(grid[0])

        queue = collections.deque()
        direction = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                     (2, 1), (2, -1), (-2, 1), (-2, -1)]

        queue.append((source.x, source.y, 0))

        while queue:
            x, y, count = queue.popleft()

            if x == destination.x and y == destination.y:
                return count

            for d in direction:
                nx, ny = x + d[0], y + d[1]

                if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    queue.append((nx, ny, count + 1))

        return -1
