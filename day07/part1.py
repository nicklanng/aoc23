import operator
from collections import Counter

with open('input') as f:
    lines = [line.rstrip() for line in f]


cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def cards_to_score(hand):
    score = 0
    for i, card in enumerate(hand):
        score += cards.index(card) << 4*(len(hand)-i-1)
    return score


def eval_hand(hand):
    data = Counter(hand)
    common = data.most_common(2)
    most_common = common[0]
    match most_common[1]:
        case 5:
            return 1000000 * 6 * 1000 + cards_to_score(hand)
        case 4:
            return 1000000 * 5 * 1000 + cards_to_score(hand)
        case 3:
            second_most_common = common[1]
            if second_most_common[1] == 2: 
                return 1000000 * 4 * 1000 + cards_to_score(hand)
            return 1000000 * 3 * 1000 + cards_to_score(hand)
        case 2:
            second_most_common = common[1]
            if second_most_common[1] == 2: 
                return 1000000 * 2 * 1000 + cards_to_score(hand)
            return 1000000 * 1 * 1000 + cards_to_score(hand)
        case 1:
            return 1000000 * 0 * 1000 + cards_to_score(hand)    


hands_to_bid = {}
hands_to_score = {}

for line in lines:
    [hand, bid] = line.split()
    hands_to_bid[hand] = int(bid)
    if hand in hands_to_score:
        print('yes')
    hands_to_score[hand] = eval_hand(hand)

sorted_hands = list(dict(sorted(hands_to_score.items(), key=operator.itemgetter(1))).keys())

total = 0
for hand, bid in hands_to_bid.items():
    rank = sorted_hands.index(hand) + 1
    print(hand, rank, bid)
    total += rank * bid

print(total)