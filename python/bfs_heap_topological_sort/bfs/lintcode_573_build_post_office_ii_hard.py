"""
author: Wei Li
date: 10/20/2020

https://www.lintcode.com/problem/build-post-office-ii

573. Build Post Office II

Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

Return the smallest sum of distance. Return -1 if it is not possible.

样例
Example 1:
Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
Output：8
Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.

Example 2:
Input：[[0,1,0],[1,0,1],[0,1,0]]
Output：4

Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
注意事项
You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.

"""
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])
    
        # 1, find out how many empty spaces and houses
        empty_spaces = []
        houses = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty_spaces.append((i, j, 0))
                elif grid[i][j] == 1:
                    houses.append((i, j))
        
        # If no empty spaces, return -1            
        if not empty_spaces:
            return -1
        
        # init a hash map to store the shortestDistance from the mail office to the house 
        shortest = sys.maxsize
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for empty_space in empty_spaces:
            distance = self.bfs(empty_space, grid, houses)
            if distance:
                shortest = min(shortest, distance)

        if shortest == sys.maxsize:
            return -1
        
        return shortest
            
    
    def is_in_bound(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def bfs(self, empty_space, grid, houses):
        hash_map = {}
        distance = 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue = collections.deque([empty_space])
        visited = set([(empty_space[0], empty_space[1])])
        
        while queue:
            x, y, path = queue.popleft()
            
            for d in directions:
                dx, dy = x + d[0], y + d[1]
       
                if self.is_in_bound(dx, dy, grid) and (dx, dy) not in visited:
                    if (dx, dy) in houses:
                        if (dx, dy) not in hash_map:
                            hash_map[(dx, dy)] = path + 1
                            distance += path + 1
                    elif grid[dx][dy] == 2:
                        continue
                    else:    
                        visited.add((dx, dy))
                        queue.append((dx, dy, path + 1))
        
        # If not all the house can get to 
        if len(hash_map) != len(houses):
            return None
        else:
            return distance


# 2
WALL = 2
HOUSE = 1
EMPTY = 0

DR = [0,-1,0,1]
DC = [-1,0,1,0]

def shortestDistance(self, grid):
    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        return -1
    
    m = len(grid)
    n = len(grid[0])
    
    dist_sum = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    
    counter = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == self.HOUSE:
                counter += 1
                self.bfs(grid,i,j, dist_sum, visited)
                
    import sys
    res = sys.maxsize
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == self.EMPTY and visited[i][j] == counter:
                res = min(res, dist_sum[i][j])
    
    return -1 if res == sys.maxsize else res
        
    
def bfs(self, grid, pos_r, pos_c, dist_sum, visited):
    m = len(grid)
    n = len(grid[0])
    
    import queue
    q = queue.Queue()
    
    is_visited = [[False] * n for _ in range(m)]
    
    q.put((pos_r,pos_c))
    
    level = 0
    while not q.empty():
        level += 1
        size = q.qsize()
        for _ in range(size):
            (cur_r, cur_c) = q.get()
            for i in range(4):
                r = cur_r + self.DR[i]
                c = cur_c + self.DC[i]
                if r >= 0 and r < m and c >= 0 and c < n and not is_visited[r][c] and grid[r][c] == self.EMPTY:
                    visited[r][c] += 1
                    dist_sum[r][c] += level
                    
                    is_visited[r][c] = True
                    q.put((r,c))