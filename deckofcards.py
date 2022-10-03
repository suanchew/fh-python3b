import random

class Card:
    def __init__(self, suit, valu):
        self.suit = suit
        self.value = valu

    def show(self):
        print ("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build52()

    def build52(self):
        for s in ["hearts", "diamonds", "clubs", "spades"]:
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(s, v))
 
    def show(self):
        for c in self.cards:
            c.show()

    def dealCard(self):
        self.cards.pop()

# Fisher-Yates shuffle algortihm
# To shuffle an array a of n elements (indices 0..n-1):
#     for i from n - 1 downto 1 do
#         j = random integer with 0 <= j <= i
#             exchange a[j] and a[i]
    def shuffle(self):
        for i in (len(self.cards)-1, 0, -1):
            for r in random.randint(0, i):
                self.cards[i], self.cards[r] = self.cards[r], self.cards[r]


def main():
    
    print ("Name: Suan Chew")
    print ("Student ID: 20153703")
    print ("Email: suanschew@gmail.com")
    print ("Course policies: " + "this is course policies")

    myDeck = Deck()
    myDeck.show()
    myDeck.shuffle()
    myDeck.show()
    myDeck.dealCard()
