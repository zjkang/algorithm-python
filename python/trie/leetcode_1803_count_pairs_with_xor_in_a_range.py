
"""
author: Zhengjian Kang
date: 03/24/2021

残酷群每日一题: 03/23/2021

https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

1803. Count Pairs With XOR in a Range

note: xor + trie + upper_bound
https://github.com/wisdompeak/LeetCode/tree/master/Trie/1803.Count-Pairs-With-XOR-in-a-Range

Given a (0-indexed) integer array nums and two integers low and high, return
the number of nice pairs.
A nice pair is a pair (i, j) where 0 <= i < j < nums.length and
low <= (nums[i] XOR nums[j]) <= high.

Example 1:
Input: nums = [1,4,2,7], low = 2, high = 6
Output: 6
Explanation: All nice pairs (i, j) are as follows:
    - (0, 1): nums[0] XOR nums[1] = 5
    - (0, 2): nums[0] XOR nums[2] = 3
    - (0, 3): nums[0] XOR nums[3] = 6
    - (1, 2): nums[1] XOR nums[2] = 6
    - (1, 3): nums[1] XOR nums[3] = 3
    - (2, 3): nums[2] XOR nums[3] = 5

Example 2:
Input: nums = [9,8,4,2,1], low = 5, high = 14
Output: 8
Explanation: All nice pairs (i, j) are as follows:
​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
    - (0, 3): nums[0] XOR nums[3] = 11
    - (0, 4): nums[0] XOR nums[4] = 8
    - (1, 2): nums[1] XOR nums[2] = 12
    - (1, 3): nums[1] XOR nums[3] = 10
    - (1, 4): nums[1] XOR nums[4] = 9
    - (2, 3): nums[2] XOR nums[3] = 6
    - (2, 4): nums[2] XOR nums[4] = 5

Constraints:
1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 2 * 10^4
1 <= low <= high <= 2 * 10^4
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.cnt = 0


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        return self.count_smaller_pairs(nums, high+1) - self.count_smaller_pairs(nums, low)

    def count_smaller_pairs(self, nums, th):
        root = TrieNode()
        count = 0
        for num in nums:  # fix j
            count += self.count_smaller_than(root, num, th)
            self.insert(root, num)
        return count

    def count_smaller_than(self, root, num, th):
        node = root
        count = 0
        for i in range(14, -1, -1):
            if not node:
                break
            c = (th >> i) & 1
            b = (num >> i) & 1
            if c == 1 and b == 0:
                if node.children[0]:
                    count += node.children[0].cnt
                node = node.children[1]
            elif c == 1 and b == 1:
                if node.children[1]:
                    count += node.children[1].cnt
                node = node.children[0]
            elif c == 0 and b == 0:
                node = node.children[0]
            elif c == 0 and b == 1:
                node = node.children[1]
        return count

    def insert(self, root, num):
        node = root
        for i in range(14, -1, -1):
            bit = (num >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.cnt += 1
