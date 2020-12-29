"""
author: Wei Li
date: 10/20/2020

https://www.lintcode.com/problem/zombie-in-matrix/

598. Zombie in Matrix
Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0
(the number zero, one, two).Zombies can turn the nearest people
(up/down/left/right) into zombies every day, but can not through wall.
How long will it take to turn all people into zombies? Return -1 if can not
turn all people into zombies.

样例
Example 1:
Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output:
2

Example 2:
Input:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
Output:
4
"""


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        M = len(grid)
        N = len(grid[0])

        queue = self.build_queue(grid, M, N)

        longest = self.get_longeset_time(queue, grid, M, N)

        if self.check_no_zeros(grid, M, N):
            return longest

        return -1

    def build_queue(self, grid, M, N):
        import collections
        queue = collections.deque()

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))

        return queue

    def get_longeset_time(self, queue, grid, M, N):
        import sys
        longest = -sys.maxsize
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            x, y, time = queue.popleft()

            longest = max(longest, time)

            for d in directions:
                nx, ny = x + d[0], y + d[1]

                if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    queue.append((nx, ny, time + 1))

        return longest

    def check_no_zeros(self, grid, M, N):
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    return False
        return True
