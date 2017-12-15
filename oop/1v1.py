# All blackjack logic in one class
# PRO: clean 'library', easy to implement
# CONS: complicated bussiness logic, not easy to read
#       if another game needs blackjack deck or hand or card has to reimplement logic
#       a game that implement blackjack with a different deck or hand has to implment everything
#       Blackjack class makes assumptions about the initial value of the cards
#       long method calls
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

    def addCard(self, card):
        self.hand.append(card)

    def getAll(self):
        return copy.deepcopy(self.hand)


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
        if self._isBlackjack(self.player) or self._isBlackjack(self.dealer):
            self.stand()

    def hit(self):
        self.player.addCard(self.deck.getNext())
        if self._getSum(self.player) => 21:
            self.stand()

    def stand(self):
        if self._isBusted(self.player):
            return -1
        if self._isBlackjack(self.player) and not self._isBlackjack(self.dealer):
            return 1
        if self._isBlackjack(self.player) and self._isBlackjack(self.dealer):
            return 0
        if not self._isBlackjack(self.player) and self._isBlackjack(self.dealer):
            return -1

        self._playDealer()

        if self._getSum(self.dealer) == self._getSum(self.player):
            return 0
        if 21 >= self._getSum(self.dealer) > self._getSum(self.player):
            return -1
        return 1

    def _isBusted(self, hand):
        return self._getSum(hand) > 21

    def _playDealer(self):
        while self._getSum(self.dealer) < self._getSum(self.player):
            self._hitDealer()


    def _getSum(self, hand):
        # return biggest value < 21 or smallest > 21
        minGreater, maxSmaler = 31, 0
        all = self._getPossibleScores(hand):
        for poss in all:
            if 21 >= poss > minGreater:
                minGreater = poss
            if 21 < poss < maxSmaler:
                maxSmaler = poss
        if maxSmaler > 0:
            return maxSmaler
        return minGreater

    def _getPossibleScores(self, hand):
        poss_scores = [0]
        for card in hand:
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

    def _isBlackjack(self, player):
        return len(self.player.getAll()) == 2 and self._getSum(player) == 21

    def _hitDealer(self):
        self.dealer.addCard(self.deck.getNext())

    def seeHand(self):
        return self.player.getAll()
