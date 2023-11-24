"""
author: Zhengjian Kang
date: 10/23/2020

https://leetcode.com/problems/word-ladder-ii/

126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list,
find all shortest transformation sequence(s) from beginWord to endWord, such
that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not
a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible
transformation.
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if beginWord == endWord:
            return []
        res = []
        word_map = {}
        self.bfs(beginWord, endWord, wordList, word_map)
        if endWord not in word_map:
            return []
        self.dfs(endWord, beginWord, word_map, [], res)
        return res

    def dfs(self, curWord, endWord, word_map, cur_res, res):
        if curWord == endWord:
            cur_res.append(curWord)
            res.append(cur_res[::-1])
            cur_res.pop()
            return
        cur_res.append(curWord)
        for w in word_map[curWord]:
            self.dfs(w, endWord, word_map, cur_res, res)
        cur_res.pop()

    def bfs(self, beginWord, endWord, wordList, word_map):
        from collections import deque
        wordList = set(wordList)
        queue = deque([beginWord])
        visited = {beginWord: 0}  # {word: step}
        while queue and endWord not in visited:
            size = len(queue)
            for _ in range(size):
                cur_word = queue.popleft()
                step = visited[cur_word]
                next_words = self.get_words(cur_word, wordList)
                for w in next_words:
                    if w not in word_map:
                        word_map[w] = []
                    if w not in visited:
                        word_map[w].append(cur_word)
                        visited[w] = step + 1
                        queue.append(w)
                    # next被同层的点加入到queue，但是我们仍然更新cur-next的关系
                    elif visited[w] == visited[cur_word] + 1:
                        word_map[w].append(cur_word)

    def get_words(self, word, wordList):
        res = []
        for i in range(len(word)):
            for j in range(26):
                letter = chr(ord('a') + j)
                if letter != word[i]:
                    new_word = word[:i] + letter + word[i+1:]
                    if new_word in wordList:
                        res.append(new_word)
        return res
