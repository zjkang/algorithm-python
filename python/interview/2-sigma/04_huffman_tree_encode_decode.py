# -------------------
# s = "aaaaabbbbcccdde"
# a = '00', b = '01', c='11', d='100', e='101'
# len(s) * 8
# len(encode(s))

class TreeNode:
    def __init__(self, letter=None, weight=None, left=None, right=None):
        self.letter = letter
        self.weight = weight
        self.left = left
        self.right = right
        
    def __lt__(self, o):
        return self.weight < o.weight

from collections import Counter
import heapq

root = None
def encode(s):
    counter = Counter(s)
    global root
    root = construct(counter)
    encoder = {}
    get_encode(root, [], encoder)
    # print(encoder)
    res = []
    for c in s:
        res.append(encoder[c])
    return ''.join(res)
    
def get_encode(root, cur, encoder):
    if not root: return
    if not root.left and not root.right:
        encoder[root.letter] = ''.join(cur)
        return
    cur.append('0')
    get_encode(root.left, cur, encoder)
    cur.pop()
    
    cur.append('1')
    get_encode(root.right, cur, encoder)
    cur.pop()
    
def construct(counter):
    pq = [TreeNode(k, v) for k, v in counter.items()]
    heapq.heapify(pq)
    while len(pq) > 1:
        n1 = heapq.heappop(pq)
        n2 = heapq.heappop(pq)
        new_node = TreeNode(None, n1.weight+n2.weight)
        new_node.left = n1
        new_node.right = n2
        heapq.heappush(pq, new_node)
    return pq[0]

def decode(s):
    res = []
    cur = root
    for c in s:
        if c == '0':
            cur = cur.left
        else:
            cur = cur.right
        if not cur.left and not cur.right:
            res.append(cur.letter)
            cur = root
    return ''.join(res)
    
s = "aaaaabbbbcccdde"
encode_s = encode(s)
print(encode_s)
print(decode(encode_s))
