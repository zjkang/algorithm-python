
"""
author: Zhengjian Kang
date: 03/08/2021

残酷群每日一题: 03/07/2021

https://leetcode.com/problems/trapping-rain-water/

42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
0 <= n <= 3 * 10^4
0 <= height[i] <= 10^5
"""


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         l, r = 0, len(height) - 1
#         res, left_max, right_max = 0, 0, 0
#         while l < r:
#             left_max = max(left_max, height[l])
#             right_max = max(right_max, height[r])
#             if left_max < right_max:
#                 res += left_max - height[l]
#                 l += 1
#             else:
#                 res += right_max - height[r]
#                 r -= 1
#         return res


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Mark the first island with '#'s
        def dfs(row, col):
            if row not in range(rows) or col not in range(cols) or grid[row][col] != 1:
                return False

            grid[row][col] = '#'
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

    # If the inner loop does not break, the outer loop will not either.
    # The for-else clause only happens if the inner loop does not break. Then continue avoids the outer break too.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    break
            else:
                continue  # only executed if the inner loop did NOT break
            break  # only executed if the inner loop DID break

            # Now let's expand from the first island we just marked and return the second we see the second island
        shortest_bridge_distance = 0
        q = deque([(r, c, shortest_bridge_distance) for r in range(rows)
                   for c in range(cols) if grid[r][c] == '#'])

        visited = set()
        while q:
            row, col, shortest_bridge_distance = q.popleft()
            directions = ((row+1, col), (row-1, col),
                          (row, col+1), (row, col-1))

            for new_row, new_col in directions:
                if new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in visited:
                    if grid[new_row][new_col] == 1:
                        return shortest_bridge_distance

                    q.append((new_row, new_col, shortest_bridge_distance+1))
                    visited.add((new_row, new_col))
