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
        #if i == len(word) - 1:
    root.leaf = True

def build_trie(words):
    root = TrieNode()
    for w in words:
        add_word(root, w)
    return root
