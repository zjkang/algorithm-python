"""
author: Wei Li
date: 10/08/2020

https://www.lintcode.com/problem/subsets/

17. Subsets

Given a set of distinct integers, return all possible subsets.

Example 1:

Input: [0]
Output:
[
  [],
  [0]
]
Example 2:

Input: [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Challenge:
Can you do it in both recursively and iteratively?

Constrains:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
"""


class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        nums.sort()
        ans = []
        self.helper(nums, 0, [], ans)

        return ans

    def helper(self, nums, index, formed, ans):
        ans.append(formed[:])

        for i in range(index, len(nums)):
            formed.append(nums[i])
            self.helper(nums, i + 1, formed, ans)
            formed.pop()


# BFS approach
class Solution2:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # write your code here
        nums.sort()
        queue = collections.deque([(0, [])])

        ans = []
        while queue:
            i, path = queue.pop()

            if i == len(nums):
                ans.append(path)
                continue

            queue.append((i + 1, path))
            queue.append((i + 1, path + [nums[i]]))

        return ans


# DFS method II
class Solution3:
    def subsets(self, nums):
        self.result = []
        self.search(sorted(nums), 0, [])
        return self.result

    def dfs(self, nums, index, oneset):
        if index == len(nums):
            self.result.append(list(oneset))
            return
        # select nums[index]
        oneset.append(nums[index])
        self.dfs(nums, index + 1, oneset)
        oneset.pop()
        # not select nums[index]
        self.dfs(nums, index + 1, oneset)
