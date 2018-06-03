import random


class Card:

    suits = ['S','H','D','C']
    faces = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    values = [11,  10,  10,  10,   10,   9,   8,   7,   6,   5,   4,   3,  2]

    face_sort_order = dict(zip(faces, range(0, len(faces))))
    suit_sort_order = dict(zip(suits, range(0,len(suits))))

    def __init__(self, face_suit):
        self.face, self.suit = face_suit.split('-')

    def __eq__(self, other):
        return self.face == other.face and self.suit == other.suit

    def __str__(self):
        return self.face + '-' + self.suit

    def sort_key(self):
        return Card.suit_sort_order[self.suit] * 100 + Card.face_sort_order[self.face]

    def value(self):
        return Card.values[Card.face_sort_order[self.face]]


class Deck:

    def __init__(self):
        self.cards = []
        self.top = 0
        for suit in Card.suits:
            for face in Card.faces:
                self.cards.append((Card(face + '-' + suit)))

    def __eq__(self,other):
        if len(self.cards) != len(other.cards):
            return False
        for i in range(0, len(self.cards)):
            if self.cards[i] != other.cards[i]:
                return False
        return True

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        result = str(self.cards[0])
        for i in range(1, len(self.cards)):
            result += " " + str(self.cards[i])
        return result

    def shuffle(self):
        for i in range(0,len(self)):
            j = random.randint(0,51)
            self.cards[i],self.cards[j] = self.cards[j],self.cards[i]

    def sort(self):
        self.cards.sort(key=lambda card: card.sort_key())

    def deal_one(self):
        result = self.cards[self.top]
        self.top += 1
        return result


class AbstractHand:

    def __init__(self, args):
        self.cards = []
        if len(args) == 0:
            return
        if isinstance(args[0], Deck):
            deck = args[0]

            card = deck.deal_one()
            self.cards.append(card)

            card = deck.deal_one()
            self.cards.append(card)
        else:
            for text in args:
                card = Card(text)
                self.cards.append(card)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        if len(self.cards) == 0:
            return ""
        result = str(self.cards[0])
        for i in range(1, len(self.cards)):
            result += " " + str(self.cards[i])
        return result

    def append(self, card):
        self.cards.append(card)

    def value(self):
        result = 0
        for card in self.cards:
            result += card.value()
        for card in self.cards:
            if result <= 21:
                break
            if card.face == 'A':
                result -= 10
        return result


class PlayerHand(AbstractHand):

    def __init__(self, *args):
        super().__init__(args)


class DealerHand(AbstractHand):

    def __init__(self, *args):
        super().__init__(args)
        self.closed = True

    def __str__(self):
        text = super().__str__()
        if self.closed:
            space_loc = text.find(" ")
            text = "*-*" + text[space_loc:]
        return text

    def open(self):
        self.closed = False


class Game:

    def __init__(self):
        self.deck = Deck()
        self.dealer_hand = None
        self.player_hand = None
        self.player_done = False
        self.dealer_done = False

    def display(self): # pragma: no cover
        print()
        text = str(self.dealer_hand)
        print(f"Dealer: {text}")
        text = str(self.player_hand)
        print(f"Player: {text}")

    def player_play_card(self): # pragma: no cover
        text = input("Do you want a card? ")
        if text.lower() == 'y':
            card = self.deck.deal_one()
            self.player_hand.append(card)
        else:
            self.player_done = True

    def player_value_test(self):
        player_value = self.player_hand.value()
        if player_value == 21:
            self.player_done = True
            text = "BLACKJACK!"
        elif player_value > 21:
            self.player_done = True
            text = "BUST!"
        else:
            text = ""
        return text

    def player_play(self): # pragma: no cover
            self.player_done = False
            while not self.player_done:
                self.display()
                text = self.player_value_test()
                if self.player_done:
                    break
                else:
                    self.player_play_card()
            return text

    def dealer_play_card(self):
        card = self.deck.deal_one()
        self.dealer_hand.append(card)

    def dealer_value_test(self, player_value):
        text = ""
        dealer_value = self.dealer_hand.value()
        if dealer_value > 21:
            text = "Player wins"
        elif dealer_value > player_value:
            text = "Dealer wins"
        elif dealer_value == player_value:
            text = "Push"
        return text

    def dealer_play(self): # pragma: no cover
        self.dealer_done = False
        player_value = self.player_hand.value()
        self.dealer_hand.open()
        text = ""
        while not self.dealer_done:
            self.display()
            text = self.dealer_value_test(player_value)

            if len(text) > 0:
                break
            else:
                self.dealer_play_card()
        return text

    def play(self): # pragma: no cover
        while True:
            self.deck.shuffle()
            self.dealer_hand = DealerHand(self.deck)
            self.player_hand = PlayerHand(self.deck)

            text = self.player_play()
            if text == "BLACKJACK!" or text == "BUST!":
                print(text)
            else:
                text = self.dealer_play()
                print(text)

            text = input("Go again? ")
            if text.lower() != "y":
                break;

if __name__ == '__main__': # pragma: no cover
    game = Game()

    game.play()
