"""
author: Wei Li
date: 10/20/2020

https://leetcode.com/problems/number-of-islands/

200. Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        ans = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                
                if curr == "1":
                    queue = collections.deque([(i, j)])
                    ans += 1
                    
                    while queue:
                        x, y = queue.popleft()
                        
                        for d in directions:
                            dx, dy = x + d[0], y + d[1]
                            if self.isInBound(dx, dy, grid) and grid[dx][dy] == "1":
                                grid[dx][dy] = "0"
                                queue.append((dx, dy))
        
        return ans
                            
    def isInBound(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])