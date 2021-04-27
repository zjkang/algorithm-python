'''

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

        
