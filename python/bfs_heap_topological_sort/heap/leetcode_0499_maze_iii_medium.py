"""
author: Zhengjian Kang
date: 10/22/2020

https://leetcode.com/problems/the-maze-iii/

499. The Maze III

There is a ball in a maze with empty spaces and walls. The ball can go through
empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't
stop rolling until hitting a wall. When the ball stops, it could choose the
next direction. There is also a hole in this maze. The ball will drop into the
hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball
could drop into the hole by moving the shortest distance. The distance is
defined by the number of empty spaces traveled by the ball from the start
position (excluded) to the hole (included). Output the moving directions
by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest
ways, you should output the lexicographically smallest way. If the ball cannot
reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the
empty space. You may assume that the borders of the maze are all walls. The
ball and the hole coordinates are represented by row and column indexes.

Example 1:
Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".

Example 2:
Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

Output: "impossible"

Explanation: The ball cannot reach the hole.

Note:

There is only one ball and one hole in the maze.
Both the ball and hole exist on an empty space, and they will not be at the
same position initially.
The given maze does not contain border (like the red rectangle in the example
pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and the width and the height of the
maze won't exceed 30.
"""


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        if ball == hole:
            return ''
        import heapq
        queue = [(0, '', ball[0], ball[1])]  # dist, path, x, y,
        dequeued = set()
        while queue:
            dist, path, x, y = heapq.heappop(queue)
            dequeued.add((x, y))
            if [x, y] == hole:
                return path
            for n_dist, n_x, n_y, n_d in self.get_next_locations(
                    maze, x, y, hole):
                if (n_x, n_y) in dequeued:
                    continue
                heapq.heappush(queue, (dist+n_dist, path+n_d, n_x, n_y))
        return 'impossible'

    def get_next_locations(self, maze, x, y, hole):
        dr = ['l', 'u', 'r', 'd']
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        next_locs = []
        for i in range(4):
            cx = x
            cy = y
            dist = 0
            while self.is_in_bound(cx, cy, maze) and maze[cx][cy] == 0:
                cx = cx + dx[i]
                cy = cy + dy[i]
                dist += 1
                if [cx, cy] == hole:
                    return [[dist, cx, cy, dr[i]]]
            # roll to the wall
            cx = cx - dx[i]
            cy = cy - dy[i]
            dist -= 1
            if cx != x or cy != y:
                next_locs.append([dist, cx, cy, dr[i]])
        return next_locs

    def is_in_bound(self, x, y, maze):
        return x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0])
