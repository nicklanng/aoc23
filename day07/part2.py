import operator
from collections import Counter

with open('input') as f:
    lines = [line.rstrip() for line in f]


cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def cards_to_score(hand):
    score = 0
    for i, card in enumerate(hand):
        score += cards.index(card) << 4*(len(hand)-i-1)
    return score


def eval_hand(hand):
    card_score = cards_to_score(hand) 

    jokers = hand.count('J')
    hand = list(filter(lambda a: a != 'J', hand))
    
    # special case for if all jokers
    if len(hand) == 0:
        return 1000000 * 6 * 1000 + card_score

    data = Counter(hand)
    common = data.most_common(2)
    most_common = common[0]

    rank = 0
    match most_common[1]:
        case 5:
            rank = 6 # five of a kind
        case 4:
            rank = 5  # four of a kind
            if jokers > 0:
                rank = 6 # bump up to a 5 of a kind
        case 3:
            if len(common) > 1 and common[1][1] == 2: 
                rank = 4 # full house
            else:
                rank = 3 # three of a kind
                if jokers == 1:
                    rank = 5 # bump to four of a kind
                if jokers == 2:
                    rank = 6 # bump to five of a kind
        case 2:
            if len(common) > 1 and common[1][1] == 2: 
                rank = 2 # two pair
                if jokers > 0:
                    rank = 4 # if the fifth card is a joker, best we can do is full house
            else:
                rank = 1 # pair
                if jokers == 1:
                    rank = 3 # bump to three of a kind
                if jokers == 2:
                    rank = 5 # bump to four of a kind
                if jokers == 3:
                    rank = 6 # bump to five of a kind
        case 1:
            rank = 0 # highest card
            if jokers == 1:
                rank = 1 # bump to pair
            if jokers == 2:
                rank = 3 # bump to three of a kind
            if jokers == 3:
                rank = 4 # bump to four of a kind
            if jokers == 4:
                rank = 6 # bump to five of a kind
         
    return 1000000 * rank * 1000 + card_score


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