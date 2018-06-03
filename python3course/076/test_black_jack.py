import unittest
import black_jack


class TestBlackJack(unittest.TestCase):

    # Card tests
    def test_card_init(self):
        card = black_jack.Card('A-S')
        self.assertTrue(card.face == 'A')
        self.assertTrue(card.suit == 'S')

    def test_card_eq(self):
        card1 = black_jack.Card('A-S')
        card2 = black_jack.Card('2-C')
        self.assertNotEqual(card1, card2)
        self.assertEqual(card1, card1)

    def test_card_str(self):
        card = black_jack.Card('Q-H')
        theStr = str(card)
        self.assertEqual(theStr, 'Q-H')

    def test_card_sort_key(self):
        card = black_jack.Card('A-S')
        sort_key = card.sort_key()
        self.assertTrue(sort_key == 0)

        card = black_jack.Card('2-C')
        sort_key = card.sort_key()
        self.assertTrue(sort_key == 312)

    def test_card_value(self):
        card = black_jack.Card('A-D')
        value = card.value()
        self.assertEqual(value, 11)

        card = black_jack.Card('8-C')
        value = card.value()
        self.assertEqual(value, 8)

    def test_card(self):
        test_black_jack.test_card_init()
        test_black_jack.test_card_eq()
        test_black_jack.test_card_str()
        test_black_jack.test_card_sort_key()
        test_black_jack.test_card_value()

    # Deck tests
    def test_deck_init(self):
        deck = black_jack.Deck()
        self.assertEqual(len(deck), 52)
        self.assertEqual(deck.cards[0], black_jack.Card('A-S'))
        self.assertEqual(deck.cards[51], black_jack.Card('2-C'))

    def test_deck_eq(self):
        deck1 = black_jack.Deck()
        deck2 = black_jack.Deck()
        self.assertEqual(deck1, deck2)

        deck2.cards.pop()
        self.assertNotEqual(deck1, deck2)

    def test_deck_len(self):
        deck = black_jack.Deck()
        length = len(deck)
        self.assertEqual(length, 52)

    def test_deck_str(self):
        deck = black_jack.Deck()
        text = str(deck)
        length = len(text)
        self.assertEqual(length, 3 + 51 * (3 + 1) + 4)
        self.assertEqual(text[0:4], 'A-S ')

    def test_deck_shuffle(self):
        deck = black_jack.Deck()
        sorted_deck = black_jack.Deck()
        deck.shuffle()
        self.assertEqual(len(deck), 52)
        self.assertNotEqual(deck, sorted_deck)

    def test_deck_sort(self):
        deck = black_jack.Deck()
        sorted_deck = black_jack.Deck()
        deck.shuffle()
        self.assertNotEqual(deck, sorted_deck)
        deck.sort()
        self.assertEqual(deck, sorted_deck)

    def test_deck_deal_one(self):
        deck = black_jack.Deck()
        card = deck.deal_one()
        self.assertEqual(str(card), 'A-S')

        card = deck.deal_one()
        self.assertEqual(str(card), 'K-S')

    def test_deck(self):
        test_black_jack.test_deck_init()
        test_black_jack.test_deck_eq()
        test_black_jack.test_deck_len()
        test_black_jack.test_deck_str()
        test_black_jack.test_deck_shuffle()
        test_black_jack.test_deck_sort()
        test_black_jack.test_deck_deal_one()

    # Hand tests
    def test_player_hand_init(self):
        deck = black_jack.Deck()
        hand = black_jack.PlayerHand(deck)
        self.assertEqual(len(hand), 2)

        hand = black_jack.PlayerHand("J-C", "Q-H", "K-C")
        self.assertEqual(len(hand),3)

    def test_player_hand_len(self):
        deck = black_jack.Deck()
        hand = black_jack.PlayerHand(deck)
        length = len(hand)
        self.assertEqual(length, 2)

    def test_player_hand_str(self):
        deck = black_jack.Deck()
        hand = black_jack.PlayerHand(deck)
        text = str(hand)
        self.assertEqual(text, 'A-S K-S')

        hand = black_jack.PlayerHand()
        text = str(hand)
        self.assertEqual(text, '')

    def test_player_hand_append(self):
        deck = black_jack.Deck()
        hand = black_jack.PlayerHand(deck)
        card = black_jack.Card('10-D')
        hand.append(card)
        text = str(hand)
        self.assertEqual(text, 'A-S K-S 10-D')

    def test_player_hand_value(self):
        deck = black_jack.Deck()
        hand = black_jack.PlayerHand(deck)
        s = hand.value()
        self.assertEqual(s, 21)

        deck = black_jack.Deck()
        hand = black_jack.PlayerHand(deck)
        card = deck.deal_one()
        hand.append(card)
        s = hand.value()
        self.assertEqual(s, 21)

        deck = black_jack.Deck()
        hand = black_jack.PlayerHand(deck)
        card = black_jack.Card('8-C')
        hand.append(card)
        s = hand.value()
        self.assertEqual(s, 19)

        deck = black_jack.Deck()
        hand = black_jack.PlayerHand(deck)
        card = black_jack.Card('A-C')
        hand.append(card)
        s = hand.value()
        self.assertEqual(s, 12)

    def test_player_hand(self):
        self.test_player_hand_init()
        self.test_player_hand_len()
        self.test_player_hand_str()
        self.test_player_hand_append()
        self.test_player_hand_value()

    # DealerHand tests
    def test_dealer_hand_init(self):
        deck = black_jack.Deck()
        hand = black_jack.DealerHand(deck)
        self.assertTrue(hand.closed)

    def test_dealer_hand_str(self):
        deck = black_jack.Deck()
        hand = black_jack.DealerHand(deck)
        text = str(hand)
        self.assertEqual(text, "*-* K-S")
        hand.open()
        text = str(hand)
        self.assertEqual(text, "A-S K-S")

    def test_dealer_hand_open(self):
        deck = black_jack.Deck()
        hand = black_jack.DealerHand(deck)
        hand.open()
        self.assertFalse(hand.closed)

    def test_dealer_hand(self):
        self.test_dealer_hand_init()
        self.test_dealer_hand_str()
        self.test_dealer_hand_open()

    # Game tests
    def test_game_init(self):
        game = black_jack.Game()
        self.assertIsNotNone(game.deck)
        self.assertIsNone(game.dealer_hand)
        self.assertIsNone(game.player_hand)
        self.assertFalse(game.player_done)
        self.assertFalse(game.dealer_done)

    def test_game_player_value_test(self):
        game = black_jack.Game()
        game.player_hand = black_jack.PlayerHand()
        game.player_hand.cards = []
        game.player_hand.cards.append(black_jack.Card('A-S'))
        game.player_hand.cards.append(black_jack.Card('K-S'))
        text = game.player_value_test()
        self.assertEqual(text, "BLACKJACK!")

        game.player_hand.cards = []
        game.player_hand.cards.append(black_jack.Card('9-S'))
        game.player_hand.cards.append(black_jack.Card('K-S'))
        game.player_hand.cards.append(black_jack.Card('K-C'))
        text = game.player_value_test()
        self.assertEqual(text, "BUST!")

        game.player_hand.cards = []
        game.player_hand.cards.append(black_jack.Card('9-S'))
        game.player_hand.cards.append(black_jack.Card('K-S'))
        text = game.player_value_test()
        self.assertEqual(text, "")

    def test_game_dealer_play_card(self):
        game = black_jack.Game()
        game.dealer_hand = black_jack.DealerHand(game.deck)
        game.dealer_hand.open()
        game.dealer_play_card()
        self.assertEqual(str(game.dealer_hand), "A-S K-S Q-S")

    def test_game_dealer_value_test(self):
        game = black_jack.Game()
        game.player_hand = black_jack.PlayerHand()
        game.dealer_hand = black_jack.DealerHand()

        game.player_hand.cards = []
        game.player_hand.cards.append(black_jack.Card('9-S'))
        game.player_hand.cards.append(black_jack.Card('K-S'))
        player_value = game.player_hand.value()

        game.dealer_hand.cards = []
        game.dealer_hand.cards.append(black_jack.Card('9-D'))
        game.dealer_hand.cards.append(black_jack.Card('K-D'))
        text = game.dealer_value_test(player_value)

        self.assertEqual(text, "Push")

        game.dealer_hand.cards = []
        game.dealer_hand.cards.append(black_jack.Card('Q-D'))
        game.dealer_hand.cards.append(black_jack.Card('K-D'))
        text = game.dealer_value_test(player_value)

        self.assertEqual(text, "Dealer wins")

        game.dealer_hand.cards = []
        game.dealer_hand.cards.append(black_jack.Card('Q-D'))
        game.dealer_hand.cards.append(black_jack.Card('5-D'))
        game.dealer_hand.cards.append(black_jack.Card('K-D'))
        text = game.dealer_value_test(player_value)

        self.assertEqual(text, "Player wins")

    def test_game(self):
        self.test_game_init()
        self.test_game_player_value_test()
        self.test_game_dealer_play_card()
        self.test_game_dealer_value_test()



if __name__ == '__main__':
    test_black_jack = TestBlackJack()

    test_black_jack.test_card()
    test_black_jack.test_deck()
    test_black_jack.test_player_hand()
    test_black_jack.test_dealer_hand()
    test_black_jack.test_game()
