"""
author: Wei Li
date: 10/08/2020

https://www.lintcode.com/problem/subsets-ii/

18. Subsets

Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).

样例
Example 1:
Input: [0]
Output:
[
  [],
  [0]
]

Example 2:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Challange:
Can you do it in both recursively and iteratively?

Constraint
Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.
"""


class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        nums.sort()

        ans = []
        self.helper(nums, 0, [], ans)

        return ans

    def helper(self, nums, index, formed, ans):
        ans.append(formed[:])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            formed.append(nums[i])
            self.helper(nums, i + 1, formed, ans)
            formed.pop()


# DFS 2: binary tree with pruning
class Solution2:
    def subsetsWithDup(self, nums):
        if not nums:
            return [[]]
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, cur, res):
        if index == len(nums):
            res.append(list(cur))
            return
        cur.append(nums[index])
        self.dfs(nums, index + 1, cur, res)
        cur.pop()
        # not selected
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        self.dfs(nums, index + 1, cur, res)
