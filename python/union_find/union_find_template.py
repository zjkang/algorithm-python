# union-find
self.father = [0] * n
for i in range(n):
    self.father[i] = i

def find_father(self, x):
    if self.father[x] != x:
        self.father[x] = self.find_father(self.father[x])
    return self.father[x]

def union(self, x, y):
    x = self.father[x]
    y = self.father[y]
    if x < y:
        self.father[y] = x
    else:
        self.father[x] = y
