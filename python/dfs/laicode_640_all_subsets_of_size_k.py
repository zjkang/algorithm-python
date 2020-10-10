"""
author: Zhengjian Kang
date: 10/10/2020

https://app.laicode.io/app/problem/640

640. All Subsets of Size K

Given a set of characters represented by a String, return a list containing all subsets of the characters whose size is K.

Assumptions
There are no duplicate characters in the original set.

​Examples

Set = "abc", K = 2, all the subsets are [“ab”, “ac”, “bc”].
Set = "", K = 0, all the subsets are [""].
Set = "", K = 1, all the subsets are [].
"""


class Solution(object):
    def subSetsOfSizeK(self, set, k):
        self.result = []
        self.dfs(set, 0, [], k)
        return self.result

    def dfs(self, set, index, oneset, k):
        if len(oneset) == k:
            self.result.append("".join(oneset))
            return
        if len(set) == index:
            return
        # select set[index]
        oneset.append(set[index])
        self.dfs(set, index + 1, oneset, k)
        oneset.pop()
        # not select set[index]
        self.dfs(set, index + 1, oneset, k)
