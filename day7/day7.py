import re
from collections import Counter

inp = open("test").read()
ranks = "23456789TJQKA"

def compare_hands(l, r):
    # compare l to r
    # return -1 if l < r
    # return 0 if ==
    # return 1 if l > r
    pass

for hand, wager in re.findall(r"([AKQJT2-9]{5}) (\d+)", inp):
    print(hand)
    c = Counter(hand)
    print(c.most_common(2))
    print(wager)
    print()