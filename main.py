import random

class Card:
    def __init__(self, sui, valu):
        self.suit = sui
        self.value = valu

    def show(self):
        print ("{} {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build52()

    def build52(self):
        for s in ["hearts", "diamonds", "clubs", "spades"]:
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                "J", "Q", "K"]:
                self.cards.append(Card(s, v))
 
    def show(self):
        for c in self.cards:
            c.show()

    def deal(self):
        return self.cards.pop()

    def deckComplete(self):
        selfCards = []
        for c in self.cards:
            selfCards.append(c.value + " " + c.suit)
        for s in ["hearts", "diamonds", "clubs", "spades"]:
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                "J", "Q", "K"]:
                if not (v + " " + s) in selfCards:
                    return False
        return True

# Fisher-Yates shuffle algortihm
# To shuffle an array a of n elements (indices 0..n-1):
#     for i from n - 1 downto 1 do
#         j = random integer with 0 <= j <= i
#             exchange a[j] and a[i]
    def shuffle(self):
        if not self.deckComplete():
            return False
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        return True

print ("Name: Suan Chew")
print ("Student ID: 20153703")
print ("Email: suanschew@gmail.com")
print ("Course policy example: It is a student’s responsibility to drop himself/herself"
     + " from the class. Simply being absent from all the class activities will result in a"
     + " final grade of F.")

#myDeck = Deck()
#myDeck.shuffle()
#myDeck.deal()
#myDeck.show()
