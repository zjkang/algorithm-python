import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

# python3 -m doctest frenchdeck.doctest -v

# python的special methods(magic method)的使用例子
# 支持sequence的操作
# __getitem__ delegates to the [] operator


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
