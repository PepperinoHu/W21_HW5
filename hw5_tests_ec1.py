#########################################
##### Name: <Hu Jiaoyang> #####
##### Uniqname:<ivanhujy>#####
#########################################

import unittest
import hw5_cards_ec1

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards_ec1.Card(0, 2)
        c2 = hw5_cards_ec1.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.assertEqual(hw5_cards_ec1.Card(0,12).rank_name,'Queen')
        return hw5_cards_ec1.Card(0,12).rank_name,'Queen'
    
    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.assertEqual(hw5_cards_ec1.Card(1,12).suit_name,'Clubs')
        return hw5_cards_ec1.Card(1,12).suit_name,'Clubs'    
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.assertEqual(hw5_cards_ec1.Card(3,13).__str__(),'King of Spades')
        return hw5_cards_ec1.Card(3,13).__str__(),'King of Spades'

    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.assertEqual(len(hw5_cards_ec1.Deck().cards),52)
        return len(hw5_cards_ec1.Deck().cards),52

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        self.assertIsInstance(hw5_cards_ec1.Deck().deal_card(),hw5_cards_ec1.Card)
        return hw5_cards_ec1.Deck().deal_card(),hw5_cards_ec1.Card
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck = hw5_cards_ec1.Deck()
        deck.deal_card()
        self.assertEqual(len(deck.cards),51)
        return len(deck.cards),51   
    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck = hw5_cards_ec1.Deck()
        deck_size_before = len(deck.cards)
        card = deck.deal_card()
        deck.replace_card(card)
        deck_size_after = len(deck.cards)
        self.assertEqual(deck_size_before,deck_size_after,52)
        return deck_size_before,deck_size_after,52
    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck = hw5_cards_ec1.Deck()
        deck.replace_card(hw5_cards_ec1.Card(0,1))
        self.assertEqual(len(deck.cards),52)
        return len(deck.cards),52 
#bonus tests!
    def test_q9(self):
        '''
        test that hand is initialized properly
        '''
        new_card = hw5_cards_ec1.Card()
        hand = hw5_cards_ec1.Hand([new_card])
        self.assertEqual(hand.cards,[new_card])

    def test_add_remove(self):
        '''
        test that add_card and remove_card function functions as inteneded
        '''
        new_card = hw5_cards_ec1.Card()
        hand = hw5_cards_ec1.Hand([])
        hand.add_card(new_card)
        self.assertEqual(hand.cards,[new_card])
        hand.remove_card(new_card)
        self.assertEqual(hand.cards,[])
    
    def test_q10(self):
        '''
        test that draw function functions as intended
        '''
        deck = hw5_cards_ec1.Deck()
        hand = hw5_cards_ec1.Hand([])

        self.assertEqual(hand.cards,[])
        self.assertEqual(len(deck.cards),52)

        hand.draw(deck)
        self.assertEqual(len(hand.cards),1)
        self.assertEqual(len(deck.cards),51)

if __name__=="__main__":
    unittest.main()