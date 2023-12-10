import re
from collections import Counter
from functools import cmp_to_key, partial

inp = open("input").read()
inp = re.findall(r"([AKQJT2-9]{5}) (\d+)", inp)
ranks = "23456789TJQKA"
ranks_joker = "J23456789TQKA"
hand_ranks = [(1,1), (2,1), (2,2), (3,1), (3,2), (4,1), (5,), (5, 0)]

def get_hand_rank(hand, jokers=False):
    c = Counter(hand)
    signature = tuple(i[1] for i in c.most_common(2))
    if jokers:
        if all(c == "J" for c in hand):
            return hand_ranks.index((5, 0))
        num_jokers = c["J"]
        c.subtract({"J": num_jokers})
        signature = tuple(i[1] for i in c.most_common(2))
        signature = (signature[0] + num_jokers, signature[1])
    return hand_ranks.index(signature)

def tiebreak(l, r, jokers=False):
    use_ranks = ranks_joker if jokers else ranks
    for i in range(len(l)):
        if l[i] == r[i]:
            continue
        return use_ranks.index(l[i]) - use_ranks.index(r[i])

def compare_hands(l, r, jokers=False):
    l, r = l[0], r[0]
    left, right = get_hand_rank(l, jokers), get_hand_rank(r, jokers)
    if left == right:
        return tiebreak(l, r, jokers)
    return left - right

hands = sorted(inp, key=cmp_to_key(compare_hands))
print(sum(rank * int(hand[1]) for rank, hand in enumerate(hands, 1)))
hands = sorted(inp, key=cmp_to_key(partial(compare_hands, jokers=True)))
print(sum(rank * int(hand[1]) for rank, hand in enumerate(hands, 1)))