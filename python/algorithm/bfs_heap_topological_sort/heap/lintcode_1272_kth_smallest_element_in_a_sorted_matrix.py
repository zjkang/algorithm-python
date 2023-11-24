"""
author: Zhengjian Kang
date: 10/22/2020

https://www.lintcode.com/problem/kth-smallest-element-in-a-sorted-matrix/description

1272. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in
ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not
the kth distinct element.

Example
Example1
Input:
[[ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
8
Output: 13

Example2
Input:
[[-5]]
1
Output: -5
"""


class Solution:
    """
    @param matrix: List[List[int]]
    @param k: a integer
    @return: return a integer
    """

    def kthSmallest(self, matrix, k):
        if not matrix or not matrix[0]:
            return None
        import heapq
        min_heap = []
        visited = set()
        heapq.heappush(min_heap, (matrix[0][0], 0, 0))
        visited.add((0, 0))

        rows = len(matrix)
        cols = len(matrix[0])
        for _ in range(1, k):
            val, x, y = heapq.heappop(min_heap)
            next_min_pos = (x, y+1)
            if (self.inbound(rows, cols, next_min_pos) and
                    next_min_pos not in visited):
                visited.add(next_min_pos)
                heapq.heappush(
                    min_heap, (matrix[next_min_pos[0]][next_min_pos[1]],
                               next_min_pos[0], next_min_pos[1]))

            next_min_pos = (x+1, y)
            if self.inbound(rows, cols, next_min_pos) and next_min_pos not in visited:
                visited.add(next_min_pos)
                heapq.heappush(
                    min_heap, (matrix[next_min_pos[0]][next_min_pos[1]], next_min_pos[0], next_min_pos[1]))

        return heapq.heappop(min_heap)[0]

    def inbound(self, rows, cols, pos):
        return pos[0] >= 0 and pos[0] < rows and pos[1] >= 0 and pos[1] < cols
