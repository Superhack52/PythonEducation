#Демонстрация сочетания объектов
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
#main
card1 = Card("A", "c")
print("Объект карта:", card1)
card2 = Card("2", "c")
card3 = Card("3", "c")
card4 = Card("4", "c")
card5 = Card("5", "c")
print("Еще четыре карты:", card2, card3, card4, card5)
my_hand = Hand()
print("\nКарты в руке:", my_hand)
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nКарты в руке после добавления:", my_hand)
your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nПередал 2 карты в другую руку.")
print("Ваша рука:", your_hand)
print("Моя рука:", my_hand)
my_hand.clear()
print("После очистки у меня на руках:", my_hand)
input("Press enter to exit.")