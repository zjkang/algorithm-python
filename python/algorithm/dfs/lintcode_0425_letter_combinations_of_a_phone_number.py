"""
author: Wei Li
date: 10/10/2020

https://www.lintcode.com/problem/letter-combinations-of-a-phone-number/

425. Letter Combinations of a phone number

Given a digit string excluded 0 and 1, return all possible letter combinations
that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given
below.

样例
Example 1:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Explanation:
'2' could be 'a', 'b' or 'c'
'3' could be 'd', 'e' or 'f'

Example 2:
Input: "5"
Output: ["j", "k", "l"]
注意事项
Although the answer above is in lexicographical order, your answer could be in
any order you want.
"""


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        if not digits:
            return []

        mapping = self.build_mapping()
        ans = []
        self.dfs(digits, 0, "", ans, mapping)

        return ans

    def dfs(self, digits, index, formed, ans, mapping):
        if index == len(digits):
            ans.append(formed)
            return

        string_val = mapping[digits[index]]

        for char in string_val:
            self.dfs(digits, index + 1, formed + char, ans, mapping)

    def build_mapping(self):
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        return mapping
