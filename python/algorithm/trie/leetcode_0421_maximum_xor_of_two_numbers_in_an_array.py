
"""
author: Zhengjian Kang
date: 03/21/2021

残酷群每日一题: 03/21/2021

https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

421. Maximum XOR of Two Numbers in an Array

note: xor + trie (32 bit integer)

Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?

Example 1:
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
Input: nums = [0]
Output: 0

Example 3:
Input: nums = [2,4]
Output: 6

Example 4:
Input: nums = [8,10,2]
Output: 10

Example 5:
Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

Constraints:
1 <= nums.length <= 2 * 10^4
0 <= nums[i] <= 2^31 - 1
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 2  # [0, 1]


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # time complexity: O(n)
        root = TrieNode()
        # build trie
        for n in nums:
            node = root
            for i in range(31, -1, -1):
                bit = ((n >> i) & 1)
                if node.children[bit] is None:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        res = 0
        for n in nums:
            node = root
            max_xor_num = 0
            for i in range(31, -1, -1):
                bit = ((n >> i) & 1)
                next_bit = bit
                if node.children[1-bit]:
                    next_bit = 1-bit
                node = node.children[next_bit]
                max_xor_num |= (next_bit << i)

            res = max(res, n ^ max_xor_num)

        return res
