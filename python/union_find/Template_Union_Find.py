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

            
# function version

father = [0] * n
for i in range(n):
    father[i] = i

def find_father(x):
    if father[x] != x:
        father[x] = find_father(father[x])
    return father[x]

def union(x, y):
    x = find_father(x)
    y = find_father(y)
    if x < y:
        father[y] = x
    else:
        father[x] = y
