# union-find
class UF:
    def __init__(self, n):
        self.father = [0] * n
        for i in range(n):
            self.father[i] = i

    def find_father(self, x):
        if self.father[x] != x:
            self.father[x] = self.find_father(self.father[x])
        return self.father[x]

    def union(self, x, y):
        x = self.find_father(x)
        y = self.find_father(y)
        if x < y:
            self.father[y] = x
        else:
            self.father[x] = y
