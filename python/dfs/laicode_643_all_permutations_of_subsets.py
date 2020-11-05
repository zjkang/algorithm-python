"""
author: Zhengjian Kang
date: 10/16/2020

https://app.laicode.io/app/problem/643

643. All Permutations of Subsets

Given a string with no duplicate characters, return a list with all
permutations of the string and all its subsets.

Examples
Set = “abc”, all permutations are
[“”, “a”, “ab”, “abc”, “ac”, “acb”, “b”, “ba”, “bac”, “bc”, “bca”, “c”,
“cb”, “cba”, “ca”, “cab”].
Set = “”, all permutations are [“”].
Set = null, all permutations are []
"""


class Solution(object):
    def allPermutationsOfSubsets(self, set):
        """
        input: string set
        return: string[]
        """
        if not set:
            return []
        set = list(set)
        self.result = [""]
        self.dfs(set, 0)
        return self.result

    def dfs(self, set, index):
        if index == len(set):
            return
        for i in range(index, len(set)):
            set[index], set[i] = set[i], set[index]
            self.result.append("".join(set[:index+1]))
            self.dfs(set, index + 1)
            set[index], set[i] = set[i], set[index]
