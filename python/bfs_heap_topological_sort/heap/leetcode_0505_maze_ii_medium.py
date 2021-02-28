"""
author: Zhengjian Kang
date: 10/20/2020

残酷群每日一题: 02/15/2021

https://leetcode.com/problems/the-maze-ii/

505. The Maze II

note: BFS + PQ的题目

There is a ball in a maze with empty spaces and walls. The ball can go
through empty spaces by rolling up, down, left or right, but it won't stop
rolling until hitting a wall. When the ball stops, it could choose the next
direction.

Given the ball's start position, the destination and the maze, find the
shortest distance for the ball to stop at the destination. The distance is
defined by the number of empty spaces traveled by the ball from the start
position (excluded) to the destination (included). If the ball cannot stop at
the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the
empty space. You may assume that the borders of the maze are all walls. The
start and destination coordinates are represented by row and column indexes.

Example 1:
Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> 
down -> right.
The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:
Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not
be at the same position initially.
The given maze does not contain border (like the red rectangle in the example
pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of
the maze won't exceed 100.
"""


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if start == destination:
            return 0
        import heapq
        queue = []
        heapq.heappush(queue, (0, start[0], start[1]))  # dist, x, y
        dequeued = set()
        while queue:
            dist, x, y = heapq.heappop(queue)
            # check dequeued here, the same location can be accessed
            # by different dist in the queue
            dequeued.add((x, y))
            if [x, y] == destination:
                return dist
            for n_dist, n_x, n_y in self.get_next_locations(maze, x, y):
                if (n_x, n_y) in dequeued:
                    continue
                heapq.heappush(queue, (dist+n_dist, n_x, n_y))
        return -1

    def get_next_locations(self, maze, x, y):
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        next_locs = []
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            dist = 1
            while self.is_in_bound(cx, cy, maze) and maze[cx][cy] == 0:
                cx = cx + dx[i]
                cy = cy + dy[i]
                dist += 1
            cx = cx - dx[i]
            cy = cy - dy[i]
            dist -= 1
            if cx != x or cy != y:
                next_locs.append([dist, cx, cy])
        return next_locs

    def is_in_bound(self, x, y, maze):
        return x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0])
