'''
author: Zhengjian Kang
date: 04/27/2021

残酷群每日一题: 04/26/2021

https://leetcode.com/problems/word-search-ii/

212. Word Search II

note: dfs配合trie

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''

# Trie template
class TrieNode:
    def __init__(self):
        self.leaf = False
        self.children = {}

def add_word(root, word):
    for i in range(len(word)):
        if word[i] not in root.children:
            root.children[word[i]] = TrieNode()
        root = root.children[word[i]]
        if i == len(word) - 1:
            root.leaf = True

def build_trie(words):
    root = TrieNode()
    for w in words:
        add_word(root, w)
    return root


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = build_trie(words)
        self.res = set()
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, visited, [], root)
        return list(self.res)
        

    def dfs(self, board, x, y, visited, cur_word, root):
        if board[x][y] not in root.children: return
        m, n = len(board), len(board[0])
        visited[x][y] = True
        cur = root.children[board[x][y]]
        cur_word.append(board[x][y])
        
        if cur.leaf:
            self.res.add(''.join(cur_word))
            
        dx = [0,-1,0,1]
        dy = [-1,0,1,0]
        for i in range(4):
            cx, cy = x + dx[i], y + dy[i]
            if cx>=0 and cx<m and cy>=0 and cy<n and not visited[cx][cy]:
                self.dfs(board, cx, cy, visited, cur_word, cur)
    
        visited[x][y] = False
        cur_word.pop()
