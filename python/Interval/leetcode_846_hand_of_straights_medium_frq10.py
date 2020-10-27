"""
author: Wei Li
date: 10/17/2020

https://leetcode.com/problems/hand-of-straights/

846. Hand of Straights

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W,
and consists of W consecutive cards.

Return true if and only if she can.

Note: This question is the same as
1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

Constraints:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""

import collections


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = collections.Counter(hand)
        queue = collections.deque()
        prev, opened = -1, 0
        for card in sorted(counter):
            if opened > counter[card] or (opened > 0 and card > prev + 1):
                return False
            queue.append(counter[card] - opened)
            prev, opened = card, counter[card]
            if len(queue) == W:
                opened -= queue.popleft()
        return opened == 0


class Solution2:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W:
            return False
        from collections import Counter
        counter = Counter(hand)
        hand.sort()
        for n in hand:
            if counter[n] == 0:
                continue
            for i in range(W):
                if n + i not in counter or counter[n+i] == 0:
                    return False
                counter[n+i] -= 1
        return True
