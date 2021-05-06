# http://www.grantjenks.com/docs/sortedcontainers/introduction.html
# use SortedList
from sortedcontainers import SortedList
sl = SortedList()

sl.update([5, 1, 3, 4, 2])
# sl
# SortedList([1, 2, 3, 4, 5])
sl.add(0)
# sl
# SortedList([0, 1, 2, 3, 4, 5])

sl = SortedList('abbcccddddeeeee')
'f' in sl
# False
sl.count('e')
# 5
sl.index('c')
# 3
sl[3]
# 'c'
sl.bisect_left('d')
# 6
sl.bisect_right('d')
# 10
sl[6:10]
# ['d', 'd', 'd', 'd']
