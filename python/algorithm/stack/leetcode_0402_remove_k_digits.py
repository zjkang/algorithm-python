"""
author: Zhengjian Kang
date: 10/19/2021

残酷群每日一题: 10/14/2021

https://leetcode.com/problems/remove-k-digits/

402. Remove K Digits

note: stack with condition control (most digits to remove)

Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:
1 <= k <= num.length <= 10^5
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = [int(i) for i in list(num)]
        res = []
        n, keep = len(nums), len(nums) - k
        for i in nums:
            while k and len(res) and res[-1] > i:
                res.pop()
                k -= 1
            res.append(i)
        res = res[:keep]
        while len(res) and res[0] == 0: res.pop(0)
        return ''.join([str(i) for i in res]) if res else '0'
 
