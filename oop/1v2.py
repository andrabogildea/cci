# Blackjack logig in engine + hand
# PRO: Blackjack can be used with any type of hand
#      Operations that can be performed on a 'blackjack' hand can be reused
#      Code more readable
# CONS: BlackjackHand makes assumptions about the initial card values
from copy import copy
from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit


class Hand:
    def __init__(self):
        self.hand = []
        self.size = 0

    def addCard(self, card):
        self.hand.append(card)
        self.size += 1

    def getAll(self):
        return copy.deepcopy(self.hand)

    def getSize():
        return self.size


class Deck:
    def __init__(self, deck):
        self.deck = deck
        self.curr = 0

    def shuffle(self):
        shuffle(self.deck):
        self.curr = 0

    def getNext(self):
        if self.curr >= len(self.deck):
            self.curr = 0
        next = self.deck[self.curr]
        self.curr += 1
        return next


class RegularDeck:
    def __init__(self):
        suits = ['diamond', 'hearth', 'club', 'spade']
        values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        cards = []
        for suit in suits:
            for value in values:
                cards.append(Card(value, suit))
        self.deck = Deck(cards)

    def shuffle(self):
        self.deck.shuffle()

    def getNext(self):
        return self.deck.getNext()


class BlackjackHand:
    def __init__(self, hand):
        self.hand = hand

    def addCard(self, card):
        self.hand.addCard(card)

    def getAll(self, card):
        return self.hand.getAll()

    def _possibleScores(self):
        poss_scores = [0]
        for card in self.hand:
            new_poss_scores = []
            for poss in possible_values:
                if card.getValue() < 11:
                    new_poss_scores.append(poss + card.getValue())
                elif 9 < card.getValue() > 14:
                    new_poss_scores.append(poss + 10)
                else:
                    new_poss_scores.append(poss + 1)
                    new_poss_scores.append(poss + 11)
            poss_scores = new_poss_scores
        return poss_scores

    def score(self):
        # return biggest value < 21 or smallest > 21
        minGreater, maxSmaler = 31, 0
        all = self._possibleScores():
        for poss in all:
            if 21 >= poss > minGreater:
                minGreater = poss
            if 21 < poss < maxSmaler:
                maxSmaler = poss
        if maxSmaler > 0:
            return maxSmaler
        return minGreater

    def is21(self):
        return self.score() == 21

    def isBusted(self):
        return self.score() > 21

    def isBlackjack(self):
        return self.hand.getSize() == 2 and self.is21():

    def hasWon(self, other):
        # one is busted and the other not
        if other.isBusted() and not self.isBusted():
            return True
        if self.isBusted() and not other.isBusted():
            return False

        # one is blackjack and the other not
        if self.isBlackjack and not other.isBlackjack():
            return True
        if other.isBlackjack() and not self.isBlackjack():
            return False

        # both are <= 21
        if not self.isBusted() and not other.isBusted():
            return self.score() > other.score()

        #both are > 21:
        return self.score() < other.score()

    def isTie(self, other):
        if self.isBlackjack() and other.isBlackjack():
            return True
        return self.score() == other.score()


class Blackjack:
    def __init__(self, deck, hand_factory):
        self.deck = deck
        self.hand_factory = hand_factory
        self.player = None
        self.dealer = None

    def start(self):
        self.player = self.hand_factory()
        self.dealer = self.hand_factory()
        self.player.addCard(self.deck.getNext())
        self.player.addCard(self.deck.getNext())
        self.dealer.addCard(self.deck.getNext())
        self.dealer.addCard(self.deck.getNext())
        if self.dealer.isBlackjack() or self.player.isBlackjack():
            self.stand()

    def hit(self):
        self.player.addCard(self.deck.getNext())
        if self.player.is21() or self.player.isBusted():
            self.stand()

    def stand(self):
        self._hitDealer()
        if self.player.isTie(self.dealer):
            return 0
        1 if self.player.hasWon(self.dealer) else -1

    def _hitDealer(self):
        while 21 > self.dealer.score() <= self.player.score():
            self._hitDealer()

    def _hitD():
        self.dealer.addCarde(self.deck.getNext())
