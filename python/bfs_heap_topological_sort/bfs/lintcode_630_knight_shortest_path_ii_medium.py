"""
author: Wei Li
date: 10/20/2020

https://www.lintcode.com/problem/knight-shortest-path-ii/description?_from=ladder&&fromId=161

630. Knight Shortest Path II

Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.

样例
Example 1:

Input:
[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Output:
3
Explanation:
[0,0]->[2,1]->[0,2]->[2,3]
Example 2:

Input:
[[0,1,0],[0,0,1],[0,0,0]]
Output:
-1
说明
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)

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
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        if not grid:
            return None

        M = len(grid)
        N = len(grid[0])
     
        queue = collections.deque([(0, 0, 0)])
        
        directions = [(1, 2), (-1, 2), (2, 1), (-2, 1)]
        
        while queue:
            x, y, path = queue.popleft()
            
            if x == M - 1 and y == N - 1:
                return path
            
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                
                if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    queue.append((nx, ny, path + 1))
        
        return -1