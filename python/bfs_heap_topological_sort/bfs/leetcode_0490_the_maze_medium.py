"""
author: Zhengjian Kang
date: 10/22/2020

https://leetcode.com/problems/the-maze/

490. The Maze

There is a ball in a maze with empty spaces (represented as 0) and walls
(represented as 1). The ball can go through the empty spaces by rolling up,
down, left or right, but it won't stop rolling until hitting a wall. When the
ball stops, it could choose the next direction.

Given the maze, the ball's start position and the destination, where start =
[startrow, startcol] and destination = [destinationrow, destinationcol],
return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

Example 1:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right ->
down -> right.

Example 2:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice
that you can pass through the destination but you cannot stop there.

Example 3:
Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],
start = [4,3], destination = [0,1]
Output: false

Constraints:

1 <= maze.length, maze[i].length <= 100
maze[i][j] is 0 or 1.
start.length == 2
destination.length == 2
0 <= startrow, destinationrow <= maze.length
0 <= startcol, destinationcol <= maze[i].length
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The maze contains at least 2 empty spaces.
"""


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if start == destination:
            return True
        from collections import deque
        queue = deque([start])
        visited = set((start[0], start[1]))
        while queue:
            head = queue.popleft()
            if head == destination:
                return True
            for n in self.get_next_valid(head, maze):
                if (n[0], n[1]) not in visited:
                    queue.append(n)
                    visited.add((n[0], n[1]))
        return False

    def get_next_valid(self, cur, maze):
        m, n = len(maze), len(maze[0])
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        next_locs = []
        for i in range(4):
            cx = cur[0] + dx[i]
            cy = cur[1] + dy[i]
            while self.is_in_bound(cx, cy, maze) and maze[cx][cy] == 0:
                cx = cx + dx[i]
                cy = cy + dy[i]
            cx = cx - dx[i]
            cy = cy - dy[i]
            if cx != cur[0] or cy != cur[1]:
                next_locs.append([cx, cy])
        return next_locs

    def is_in_bound(self, x, y, maze):
        return x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0])
