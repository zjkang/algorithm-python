
"""
author: Zhengjian Kang
date: 03/18/2021

残酷群每日一题: 03/18/2021

https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

1738. Find Kth Largest XOR Coordinate Value

note: xor + dp

You are given a 2D matrix of size m x n, consisting of non-negative integers.
You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j]
where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).
Find the kth largest value (1-indexed) of all the coordinates of matrix.

Example 1:
Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the
largest value.

Example 2:
Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest
value.

Example 3:
Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is
the 3rd largest value.

Example 4:
Input: matrix = [[5,2],[1,6]], k = 4
Output: 0
Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which
is the 4th largest value.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 10^6
1 <= k <= m * n
"""


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        queue = []
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = matrix[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] ^ matrix[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] ^ matrix[i][j]
                else:
                    dp[i][j] = dp[i-1][j] ^ dp[i][j -
                                                  1] ^ dp[i-1][j-1] ^ matrix[i][j]

                heapq.heappush(queue, dp[i][j])
                if len(queue) > k:
                    heapq.heappop(queue)

        return queue[0]
