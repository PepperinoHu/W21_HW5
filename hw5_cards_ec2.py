import random
import unittest

VERSION = 0.01
 
class Card:
    '''a standard playing card
    cards will have a suit and a rank
    Class Attributes
    ----------------
    suit_names: list
        the four suit names in order 
        0:Diamonds, 1:Clubs, 2: Hearts, 3: Spades
    
    faces: dict
        maps face cards' rank name
        1:Ace, 11:Jack, 12:Queen,  13:King
    Instance Attributes
    -------------------
    suit: int
        the numerical index into the suit_names list
    suit_name: string
        the name of the card's suit
    rank: int
        the numerical rank of the card
    rank_name: string
        the name of the card's rank (e.g., "King" or "3")
    '''
    suit_names = ["Diamonds","Clubs","Hearts","Spades"]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}
 

    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.suit_name = Card.suit_names[self.suit]

        self.rank = rank
        if self.rank in Card.faces:
            self.rank_name = Card.faces[self.rank]
        else:
            self.rank_name = str(self.rank)
 
    def __str__(self):
        return f"{self.rank_name} of {self.suit_name}"
 

class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self): 

        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order
 
    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters  
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i) 
    #bonus function!
    def deal(self, num_of_hands,cards_per_hand):
        '''
        takes two parameters representing the number of hands and the number of cards per hand and returns a list of Hands. 
        If the number of cards per hand is set to -1, all of the cards should be dealt, even if this results in an uneven number of cards per hand. 
        Parameters  
        -------------------
        num_of_hands: int 
            the number of hands to be returned
        num_of_hands: int 
            number of cards per hand for the list of hands to be returned. -1 will deal all remaining cards even when it can result in uneven number of cards per hand.
        Returns
        -------
        list_of_hands
            the list of hands that are dealt
        '''
        list_of_hands = []
        if cards_per_hand != -1:
            list_of_hands = [[self.deal_card() for i in range(cards_per_hand)] for j in range(num_of_hands)]
        else:
            extra_cards = len(self.cards) % num_of_hands
            cards_per_hand = int(len(self.cards) / num_of_hands)
            print(extra_cards,cards_per_hand )
            list_of_hands = [[self.deal_card() for i in range(cards_per_hand)] for j in range(num_of_hands)]
            for i in range(extra_cards):
                list_of_hands[i].append(self.deal_card())
        for hand in list_of_hands:
            print_hand(hand)
        return list_of_hands
    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)
 
    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list
    
    def sort_cards(self):
        '''returns the Deck to its original order
        
        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
 
    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck
        
        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters  
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

def print_hand(hand):
    '''prints a hand in a compact form
    
    Parameters  
    -------------------
    hand: list
        list of Cards to print
    Returns
    -------
    none
    '''
    hand_str = '/ '
    for c in hand:
        s = c.suit_name[0]
        r = c.rank_name[0]
        hand_str += r + "of" + s + ' / '
    print(hand_str)

def remove_pairs(hand):
    '''looks for pairs of cards in a hand and removes them
    
    Parameters  
    -------------------
    hand: list
        list of Cards
    Returns
    -------
    hand_no_pair: list
        list of Cards with pairs removed
    '''
    rank_name_list = [c.rank_name[0] for c in hand]
    duplicates_set = set()
    for i in range(len(rank_name_list)):
        current_name = rank_name_list[i]
        duplicates = [x for x in rank_name_list if x == current_name]
        if len(duplicates)>1:
            duplicates_set.add((duplicates[0],len(duplicates)))
    for duplicates in duplicates_set:
        if ((duplicates[1]==4) | (duplicates[1]==2)):
            hand = [card for card in hand if card.rank_name[0] != duplicates[0]]
        if duplicates[1]==3:
            hand = [card for card in hand if card.rank_name[0] != duplicates[0]] + [[card for card in hand if card.rank_name[0] == duplicates[0]][0]]
    return hand
