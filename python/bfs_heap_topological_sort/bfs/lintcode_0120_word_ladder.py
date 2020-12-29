"""
author: Wei Li
date: 10/10/2020

https://www.lintcode.com/problem/word-ladder/
https://leetcode.com/problems/word-ladder/

120. word Ladder

Given two words (start and end), and a dictionary, find the shortest
transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary.
(Start and end words do not need to appear in the dictionary )

样例
Example 1:
Input：start = "a"，end = "c"，dict =["a","b","c"]
Output：2
Explanation：
"a"->"c"

Example 2:
Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output：5
Explanation：
"hit"->"hot"->"dot"->"dog"->"cog"

注意事项
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        if not start or not end:
            return 0
        import collections
        queue = collections.deque([(start, 1)])
        visited = set([start])

        while queue:
            word, path = queue.popleft()
            next_words = self.get_next_words(word)

            for n in next_words:
                if n == end:
                    return path

                if n in dict and n not in visited:
                    visited.add(n)
                    queue.append((n, path + 1))

        return 0

    def get_next_words(self, curr):
        words = []

        for i in range(len(curr)):
            left, right = curr[:i], curr[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if curr[i] == char:
                    continue

                words.append(left + char + right)

        return words
