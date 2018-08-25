#Демонстрация расширения класса через наследование
class Card(object):
    """Одна игральная карта"""
    RANKS = ["A", "2", "3", "4", "5", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit
    def __str__(self):
            rep = self.rank + self.suit
            return rep
class Hand(object):
    """'Рука': набор карт на руках у одного игрока."""
    def __init__(self):
            self.cards = []
    def __str__(self):
            if self.cards:
                rep = ""
                for card in self.cards:
                    rep += str(card) + " "
            else:
                rep = "<пусто>"
            return rep
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
class Deck(Hand):
    """Колода игральных карт."""
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Карты закончились.")
#основная часть
deck1 = Deck()
print("Создана новоя колода:", deck1)
deck1.populate()
print("\nВ колоде появились карты:", deck1)
deck1.shuffle()
print("Перемешаем коолоду:", deck1)
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, 5)
print("У меня руках:", my_hand)
print("У тебя на руках:", your_hand)
deck1.clear()
print("\nОчистилеи колоду", deck1)
input("\nPress enter...")